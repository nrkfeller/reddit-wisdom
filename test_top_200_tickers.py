#!/usr/bin/env python3

import sys
import os
import json
import asyncio
import aiohttp
from typing import List, Dict, Tuple

sys.path.append(os.path.join(os.path.dirname(__file__), 'reddit-stock-tracker-backend'))

from app.services.ticker_extractor import TickerExtractor
from app.services.data_processor import DataProcessor

def load_top_200_tickers() -> List[str]:
    """Load the top 200 tickers from our research"""
    top_200_tickers = [
        "AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "NVDA", "TSLA", "META", "BRK.B", "BRK.A",
        "V", "JPM", "JNJ", "WMT", "PG", "UNH", "HD", "MA", "BAC", "XOM",
        "ORCL", "CVX", "LLY", "ABBV", "KO", "AVGO", "PEP", "COST", "TMO", "MRK",
        "ACN", "CSCO", "ABT", "DHR", "TXN", "VZ", "ADBE", "NKE", "CRM", "WFC",
        "NFLX", "DIS", "INTC", "AMD", "CMCSA", "PFE", "PM", "RTX", "NEE", "UPS",
        "T", "LOW", "QCOM", "HON", "UNP", "MS", "CAT", "GS", "IBM", "AMGN",
        "BLK", "AXP", "DE", "SPGI", "BKNG", "MDT", "ADP", "GILD", "LRCX", "TJX",
        "VRTX", "SYK", "SCHW", "C", "ZTS", "MMC", "CB", "MO", "USB", "PYPL",
        "SO", "PNC", "AON", "DUK", "CSX", "TMUS", "FCX", "BMY", "NOW", "AMAT",
        "SHW", "MU", "ICE", "GE", "CME", "TGT", "REGN", "APD", "EOG", "NSC",
        "KLAC", "SLB", "MDLZ", "ADI", "ISRG", "CI", "CMG", "FISV", "TFC", "MCD",
        "CVS", "EMR", "BSX", "ITW", "WM", "GD", "MCO", "FDX", "NOC", "EQIX",
        "APH", "ECL", "PSA", "CL", "WELL", "PLD", "EL", "MCHP", "HUM", "CTAS",
        "FAST", "PAYX", "ROST", "ODFL", "VRSK", "EXC", "KMB", "CTSH", "GWW", "IDXX",
        "YUM", "BIIB", "KHC", "DXCM", "EA", "SBUX", "MNST", "EW", "ILMN", "WBA",
        "CSGP", "ANSS", "ZBH", "CPRT", "MKTX", "WLTW", "CDNS", "SNPS", "MAR", "ROP",
        "FTNT", "ADSK", "A", "MSCI", "EXR", "PCAR", "CMI", "NXPI", "ORLY", "AZO",
        "DLTR", "EBAY", "CHTR", "XLNX", "ALGN", "MXIM", "SWKS", "INCY", "SIRI", "WDC",
        "NTAP", "VIAC", "DISH", "FOXA", "FOX", "GME", "AMC", "PLTR", "BB", "NOK",
        "COIN", "HOOD", "RBLX", "SNOW", "MSTR", "RIOT", "MARA", "TSM", "ASML", "NVO",
        "SHOP", "SQ", "ROKU", "PINS", "SNAP", "TWTR", "UBER", "LYFT", "ABNB", "DASH",
        "ZM", "PTON", "DOCU", "CRWD", "OKTA", "DDOG", "NET", "TWLO", "SPLK", "WDAY",
        "VEEV", "ZS", "PANW", "TEAM", "MDB", "ESTC", "FSLY", "FVRR", "UPWK", "ETSY",
        "SPOT", "BABA", "JD", "PDD", "NIO", "XPEV", "LI"
    ]
    return top_200_tickers

def test_ticker_validation(tickers: List[str]) -> Tuple[List[str], List[str]]:
    """Test ticker validation for all tickers"""
    print("Testing ticker validation...")
    
    extractor = TickerExtractor()
    valid_tickers = []
    invalid_tickers = []
    
    for ticker in tickers:
        is_valid = extractor.validate_ticker(ticker)
        if is_valid:
            valid_tickers.append(ticker)
        else:
            invalid_tickers.append(ticker)
    
    return valid_tickers, invalid_tickers

def test_mock_data_coverage(tickers: List[str]) -> Tuple[List[str], List[str]]:
    """Test mock data coverage for all tickers"""
    print("Testing mock data coverage...")
    
    processor = DataProcessor()
    processor._initialize_mock_data()
    
    covered_tickers = []
    missing_tickers = []
    
    for ticker in tickers:
        history = processor.get_ticker_history(ticker)
        if history and len(history) > 0:
            covered_tickers.append(ticker)
        else:
            missing_tickers.append(ticker)
    
    return covered_tickers, missing_tickers

async def test_api_endpoints(tickers: List[str], base_url: str = "http://localhost:8005") -> Dict[str, List[str]]:
    """Test API endpoints for ticker validation and data retrieval"""
    print(f"Testing API endpoints at {base_url}...")
    
    results = {
        'validation_passed': [],
        'validation_failed': [],
        'history_available': [],
        'history_missing': [],
        'api_errors': []
    }
    
    async with aiohttp.ClientSession() as session:
        for ticker in tickers[:20]:  # Test first 20 to avoid overwhelming the API
            try:
                async with session.post(
                    f"{base_url}/api/ticker/validate",
                    json={"ticker": ticker}
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get('valid', False):
                            results['validation_passed'].append(ticker)
                        else:
                            results['validation_failed'].append(ticker)
                    else:
                        results['api_errors'].append(f"{ticker}: HTTP {response.status}")
            except Exception as e:
                results['api_errors'].append(f"{ticker}: {str(e)}")
        
        for ticker in tickers[:20]:  # Test first 20 to avoid overwhelming the API
            try:
                async with session.get(f"{base_url}/api/ticker/{ticker}/history") as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get('history') and len(data['history']) > 0:
                            results['history_available'].append(ticker)
                        else:
                            results['history_missing'].append(ticker)
                    else:
                        results['api_errors'].append(f"{ticker} history: HTTP {response.status}")
            except Exception as e:
                results['api_errors'].append(f"{ticker} history: {str(e)}")
    
    return results

def generate_test_report(
    tickers: List[str],
    valid_tickers: List[str],
    invalid_tickers: List[str],
    covered_tickers: List[str],
    missing_tickers: List[str],
    api_results: Dict[str, List[str]] = None
) -> str:
    """Generate a comprehensive test report"""
    
    report = []
    report.append("=" * 80)
    report.append("TOP 200 STOCK TICKERS COMPREHENSIVE TEST REPORT")
    report.append("=" * 80)
    
    report.append(f"\nSUMMARY:")
    report.append(f"Total tickers tested: {len(tickers)}")
    report.append(f"Validation passed: {len(valid_tickers)}/{len(tickers)} ({len(valid_tickers)/len(tickers)*100:.1f}%)")
    report.append(f"Mock data coverage: {len(covered_tickers)}/{len(tickers)} ({len(covered_tickers)/len(tickers)*100:.1f}%)")
    
    report.append(f"\nTICKER VALIDATION RESULTS:")
    report.append(f"✅ PASSED ({len(valid_tickers)}): {', '.join(valid_tickers[:20])}")
    if len(valid_tickers) > 20:
        report.append(f"    ... and {len(valid_tickers) - 20} more")
    
    if invalid_tickers:
        report.append(f"❌ FAILED ({len(invalid_tickers)}): {', '.join(invalid_tickers)}")
    
    report.append(f"\nMOCK DATA COVERAGE:")
    report.append(f"✅ COVERED ({len(covered_tickers)}): {', '.join(covered_tickers[:20])}")
    if len(covered_tickers) > 20:
        report.append(f"    ... and {len(covered_tickers) - 20} more")
    
    if missing_tickers:
        report.append(f"❌ MISSING ({len(missing_tickers)}): {', '.join(missing_tickers)}")
    
    if api_results:
        report.append(f"\nAPI ENDPOINT TESTS (Sample of 20 tickers):")
        report.append(f"✅ Validation API passed: {len(api_results['validation_passed'])}")
        report.append(f"❌ Validation API failed: {len(api_results['validation_failed'])}")
        report.append(f"✅ History API available: {len(api_results['history_available'])}")
        report.append(f"❌ History API missing: {len(api_results['history_missing'])}")
        
        if api_results['api_errors']:
            report.append(f"⚠️  API Errors: {len(api_results['api_errors'])}")
            for error in api_results['api_errors'][:5]:
                report.append(f"    {error}")
    
    report.append(f"\nOVERALL STATUS:")
    if len(invalid_tickers) == 0 and len(missing_tickers) == 0:
        report.append("🎉 ALL TESTS PASSED! All 200 tickers are fully supported.")
    else:
        report.append("⚠️  ISSUES FOUND:")
        if invalid_tickers:
            report.append(f"   - {len(invalid_tickers)} tickers failed validation")
        if missing_tickers:
            report.append(f"   - {len(missing_tickers)} tickers missing mock data")
    
    report.append("=" * 80)
    
    return "\n".join(report)

async def main():
    """Run comprehensive tests on top 200 tickers"""
    print("Starting comprehensive test of top 200 stock tickers...")
    
    tickers = load_top_200_tickers()
    print(f"Loaded {len(tickers)} tickers for testing")
    
    valid_tickers, invalid_tickers = test_ticker_validation(tickers)
    
    covered_tickers, missing_tickers = test_mock_data_coverage(tickers)
    
    api_results = None
    try:
        api_results = await test_api_endpoints(tickers)
    except Exception as e:
        print(f"API testing skipped (backend not running): {e}")
    
    report = generate_test_report(
        tickers, valid_tickers, invalid_tickers,
        covered_tickers, missing_tickers, api_results
    )
    
    print(report)
    
    with open('/home/ubuntu/repos/reddit-wisdom/top_200_test_report.txt', 'w') as f:
        f.write(report)
    
    print(f"\nTest report saved to: top_200_test_report.txt")
    
    return len(invalid_tickers) == 0 and len(missing_tickers) == 0

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
