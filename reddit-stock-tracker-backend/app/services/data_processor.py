from collections import defaultdict
from datetime import datetime
from typing import Dict, List


class DataProcessor:
    def __init__(self):
        self.mention_data = defaultdict(
            lambda: defaultdict(int)
        )  # {date: {ticker: count}}
        self.ticker_metadata = {}  # {ticker: {name, last_price, etc}}
        self._initialize_mock_data()

    def process_reddit_data(self, reddit_data: List[Dict], ticker_extractor):
        """Process Reddit data and extract ticker mentions by date"""
        processed_count = 0

        for item in reddit_data:
            try:
                created_utc = item.get("created_utc", 0)
                if created_utc:
                    item_date = datetime.fromtimestamp(created_utc).date()
                else:
                    continue

                text = ""
                if "title" in item:
                    text += item["title"] + " "
                if "selftext" in item:
                    text += item["selftext"] + " "
                if "body" in item:
                    text += item["body"] + " "

                if not text.strip():
                    continue

                tickers = ticker_extractor.extract_tickers(text)
                for ticker in tickers:
                    if ticker_extractor.validate_ticker(ticker):
                        self.mention_data[item_date.isoformat()][ticker] += 1
                        processed_count += 1

            except Exception as e:
                print(f"Error processing item: {e}")
                continue

        print(f"Processed {processed_count} ticker mentions")

    def get_trending_tickers(self, limit: int = 10) -> List[Dict]:
        """Get top trending tickers by total mentions"""
        ticker_totals = defaultdict(int)
        for date_data in self.mention_data.values():
            for ticker, count in date_data.items():
                ticker_totals[ticker] += count

        sorted_tickers = sorted(ticker_totals.items(), key=lambda x: x[1], reverse=True)
        return [
            {"ticker": ticker, "total_mentions": count}
            for ticker, count in sorted_tickers[:limit]
        ]

    def get_ticker_history(self, ticker: str) -> List[Dict]:
        """Get mention history for a specific ticker"""
        history = []
        for date_str, tickers in self.mention_data.items():
            count = tickers.get(ticker.upper(), 0)
            history.append({"date": date_str, "mentions": count})

        return sorted(history, key=lambda x: x["date"])

    def get_all_dates(self) -> List[str]:
        """Get all dates with data"""
        return sorted(list(self.mention_data.keys()))

    def _initialize_mock_data(self):
        """Initialize mock data for testing purposes"""
        import random
        from datetime import datetime, timedelta
        
        base_mentions = {
            'AAPL': 2500, 'MSFT': 2200, 'GOOGL': 2000, 'GOOG': 2000, 'AMZN': 1900,
            'NVDA': 2800, 'TSLA': 3000, 'META': 1800, 'BRK.B': 1200, 'BRK.A': 800,
            
            'V': 1000, 'JPM': 1100, 'JNJ': 900, 'WMT': 800, 'PG': 700,
            'UNH': 900, 'HD': 800, 'MA': 950, 'BAC': 1200, 'XOM': 1100,
            
            'GME': 2500, 'AMC': 2000, 'PLTR': 1500, 'BB': 1200, 'NOK': 1000,
            'COIN': 1800, 'HOOD': 1400, 'RBLX': 1300, 'SNOW': 1100,
        }
        
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
        
        for ticker in top_200_tickers:
            if ticker in base_mentions:
                base_count = base_mentions[ticker]
            else:
                position = top_200_tickers.index(ticker) if ticker in top_200_tickers else 100
                base_count = max(200, 1200 - (position * 4))
            
            for i in range(30):
                date = (datetime.now() - timedelta(days=29-i)).strftime('%Y-%m-%d')
                
                volatility = random.uniform(0.7, 1.3)
                daily_mentions = int(base_count * volatility)
                
                weekday = (datetime.now() - timedelta(days=29-i)).weekday()
                if weekday >= 5:  # Saturday, Sunday
                    daily_mentions = int(daily_mentions * 0.6)
                
                if date not in self.mention_data:
                    self.mention_data[date] = {}
                
                self.mention_data[date][ticker] = daily_mentions
