#!/usr/bin/env python3

import json
from typing import List, Dict, Tuple

def get_top_200_stocks() -> List[Dict[str, str]]:
    """Get comprehensive list of top 200 stocks by market cap"""
    print("Compiling top 200 stocks by market cap...")
    
    top_200_stocks = [
        {'ticker': 'AAPL', 'company': 'Apple Inc.', 'source': 'Mega Cap'},
        {'ticker': 'MSFT', 'company': 'Microsoft Corporation', 'source': 'Mega Cap'},
        {'ticker': 'GOOGL', 'company': 'Alphabet Inc. Class A', 'source': 'Mega Cap'},
        {'ticker': 'GOOG', 'company': 'Alphabet Inc. Class C', 'source': 'Mega Cap'},
        {'ticker': 'AMZN', 'company': 'Amazon.com Inc.', 'source': 'Mega Cap'},
        {'ticker': 'NVDA', 'company': 'NVIDIA Corporation', 'source': 'Mega Cap'},
        {'ticker': 'TSLA', 'company': 'Tesla Inc.', 'source': 'Mega Cap'},
        {'ticker': 'META', 'company': 'Meta Platforms Inc.', 'source': 'Mega Cap'},
        {'ticker': 'BRK.B', 'company': 'Berkshire Hathaway Class B', 'source': 'Mega Cap'},
        {'ticker': 'BRK.A', 'company': 'Berkshire Hathaway Class A', 'source': 'Mega Cap'},
        {'ticker': 'V', 'company': 'Visa Inc.', 'source': 'Mega Cap'},
        {'ticker': 'JPM', 'company': 'JPMorgan Chase & Co.', 'source': 'Mega Cap'},
        {'ticker': 'JNJ', 'company': 'Johnson & Johnson', 'source': 'Mega Cap'},
        {'ticker': 'WMT', 'company': 'Walmart Inc.', 'source': 'Mega Cap'},
        {'ticker': 'PG', 'company': 'Procter & Gamble Co.', 'source': 'Mega Cap'},
        {'ticker': 'UNH', 'company': 'UnitedHealth Group Inc.', 'source': 'Mega Cap'},
        {'ticker': 'HD', 'company': 'Home Depot Inc.', 'source': 'Mega Cap'},
        {'ticker': 'MA', 'company': 'Mastercard Inc.', 'source': 'Mega Cap'},
        {'ticker': 'BAC', 'company': 'Bank of America Corp.', 'source': 'Mega Cap'},
        {'ticker': 'XOM', 'company': 'Exxon Mobil Corporation', 'source': 'Mega Cap'},
        {'ticker': 'ORCL', 'company': 'Oracle Corporation', 'source': 'Mega Cap'},
        {'ticker': 'CVX', 'company': 'Chevron Corporation', 'source': 'Mega Cap'},
        {'ticker': 'LLY', 'company': 'Eli Lilly and Company', 'source': 'Mega Cap'},
        {'ticker': 'ABBV', 'company': 'AbbVie Inc.', 'source': 'Mega Cap'},
        {'ticker': 'KO', 'company': 'Coca-Cola Company', 'source': 'Mega Cap'},
        {'ticker': 'AVGO', 'company': 'Broadcom Inc.', 'source': 'Mega Cap'},
        {'ticker': 'PEP', 'company': 'PepsiCo Inc.', 'source': 'Mega Cap'},
        {'ticker': 'COST', 'company': 'Costco Wholesale Corporation', 'source': 'Mega Cap'},
        {'ticker': 'TMO', 'company': 'Thermo Fisher Scientific Inc.', 'source': 'Mega Cap'},
        {'ticker': 'MRK', 'company': 'Merck & Co. Inc.', 'source': 'Mega Cap'},
        {'ticker': 'ACN', 'company': 'Accenture plc', 'source': 'Mega Cap'},
        {'ticker': 'CSCO', 'company': 'Cisco Systems Inc.', 'source': 'Mega Cap'},
        {'ticker': 'ABT', 'company': 'Abbott Laboratories', 'source': 'Mega Cap'},
        {'ticker': 'DHR', 'company': 'Danaher Corporation', 'source': 'Mega Cap'},
        {'ticker': 'TXN', 'company': 'Texas Instruments Inc.', 'source': 'Mega Cap'},
        {'ticker': 'VZ', 'company': 'Verizon Communications Inc.', 'source': 'Mega Cap'},
        {'ticker': 'ADBE', 'company': 'Adobe Inc.', 'source': 'Mega Cap'},
        {'ticker': 'NKE', 'company': 'Nike Inc.', 'source': 'Mega Cap'},
        {'ticker': 'CRM', 'company': 'Salesforce Inc.', 'source': 'Mega Cap'},
        {'ticker': 'WFC', 'company': 'Wells Fargo & Company', 'source': 'Mega Cap'},
        {'ticker': 'NFLX', 'company': 'Netflix Inc.', 'source': 'Mega Cap'},
        {'ticker': 'DIS', 'company': 'Walt Disney Company', 'source': 'Mega Cap'},
        {'ticker': 'INTC', 'company': 'Intel Corporation', 'source': 'Mega Cap'},
        {'ticker': 'AMD', 'company': 'Advanced Micro Devices Inc.', 'source': 'Mega Cap'},
        {'ticker': 'CMCSA', 'company': 'Comcast Corporation', 'source': 'Mega Cap'},
        {'ticker': 'PFE', 'company': 'Pfizer Inc.', 'source': 'Mega Cap'},
        {'ticker': 'PM', 'company': 'Philip Morris International Inc.', 'source': 'Mega Cap'},
        {'ticker': 'RTX', 'company': 'Raytheon Technologies Corporation', 'source': 'Mega Cap'},
        {'ticker': 'NEE', 'company': 'NextEra Energy Inc.', 'source': 'Mega Cap'},
        {'ticker': 'UPS', 'company': 'United Parcel Service Inc.', 'source': 'Mega Cap'},
        
        {'ticker': 'T', 'company': 'AT&T Inc.', 'source': 'Large Cap'},
        {'ticker': 'LOW', 'company': 'Lowe\'s Companies Inc.', 'source': 'Large Cap'},
        {'ticker': 'QCOM', 'company': 'QUALCOMM Inc.', 'source': 'Large Cap'},
        {'ticker': 'HON', 'company': 'Honeywell International Inc.', 'source': 'Large Cap'},
        {'ticker': 'UNP', 'company': 'Union Pacific Corporation', 'source': 'Large Cap'},
        {'ticker': 'MS', 'company': 'Morgan Stanley', 'source': 'Large Cap'},
        {'ticker': 'CAT', 'company': 'Caterpillar Inc.', 'source': 'Large Cap'},
        {'ticker': 'GS', 'company': 'Goldman Sachs Group Inc.', 'source': 'Large Cap'},
        {'ticker': 'IBM', 'company': 'International Business Machines Corp.', 'source': 'Large Cap'},
        {'ticker': 'AMGN', 'company': 'Amgen Inc.', 'source': 'Large Cap'},
        {'ticker': 'BLK', 'company': 'BlackRock Inc.', 'source': 'Large Cap'},
        {'ticker': 'AXP', 'company': 'American Express Company', 'source': 'Large Cap'},
        {'ticker': 'DE', 'company': 'Deere & Company', 'source': 'Large Cap'},
        {'ticker': 'SPGI', 'company': 'S&P Global Inc.', 'source': 'Large Cap'},
        {'ticker': 'BKNG', 'company': 'Booking Holdings Inc.', 'source': 'Large Cap'},
        {'ticker': 'MDT', 'company': 'Medtronic plc', 'source': 'Large Cap'},
        {'ticker': 'ADP', 'company': 'Automatic Data Processing Inc.', 'source': 'Large Cap'},
        {'ticker': 'GILD', 'company': 'Gilead Sciences Inc.', 'source': 'Large Cap'},
        {'ticker': 'LRCX', 'company': 'Lam Research Corporation', 'source': 'Large Cap'},
        {'ticker': 'TJX', 'company': 'TJX Companies Inc.', 'source': 'Large Cap'},
        {'ticker': 'VRTX', 'company': 'Vertex Pharmaceuticals Inc.', 'source': 'Large Cap'},
        {'ticker': 'SYK', 'company': 'Stryker Corporation', 'source': 'Large Cap'},
        {'ticker': 'SCHW', 'company': 'Charles Schwab Corporation', 'source': 'Large Cap'},
        {'ticker': 'C', 'company': 'Citigroup Inc.', 'source': 'Large Cap'},
        {'ticker': 'ZTS', 'company': 'Zoetis Inc.', 'source': 'Large Cap'},
        {'ticker': 'MMC', 'company': 'Marsh & McLennan Companies Inc.', 'source': 'Large Cap'},
        {'ticker': 'CB', 'company': 'Chubb Limited', 'source': 'Large Cap'},
        {'ticker': 'MO', 'company': 'Altria Group Inc.', 'source': 'Large Cap'},
        {'ticker': 'USB', 'company': 'U.S. Bancorp', 'source': 'Large Cap'},
        {'ticker': 'PYPL', 'company': 'PayPal Holdings Inc.', 'source': 'Large Cap'},
        {'ticker': 'SO', 'company': 'Southern Company', 'source': 'Large Cap'},
        {'ticker': 'PNC', 'company': 'PNC Financial Services Group Inc.', 'source': 'Large Cap'},
        {'ticker': 'AON', 'company': 'Aon plc', 'source': 'Large Cap'},
        {'ticker': 'DUK', 'company': 'Duke Energy Corporation', 'source': 'Large Cap'},
        {'ticker': 'CSX', 'company': 'CSX Corporation', 'source': 'Large Cap'},
        {'ticker': 'TMUS', 'company': 'T-Mobile US Inc.', 'source': 'Large Cap'},
        {'ticker': 'FCX', 'company': 'Freeport-McMoRan Inc.', 'source': 'Large Cap'},
        {'ticker': 'BMY', 'company': 'Bristol-Myers Squibb Company', 'source': 'Large Cap'},
        {'ticker': 'NOW', 'company': 'ServiceNow Inc.', 'source': 'Large Cap'},
        {'ticker': 'AMAT', 'company': 'Applied Materials Inc.', 'source': 'Large Cap'},
        {'ticker': 'SHW', 'company': 'Sherwin-Williams Company', 'source': 'Large Cap'},
        {'ticker': 'MU', 'company': 'Micron Technology Inc.', 'source': 'Large Cap'},
        {'ticker': 'ICE', 'company': 'Intercontinental Exchange Inc.', 'source': 'Large Cap'},
        {'ticker': 'GE', 'company': 'General Electric Company', 'source': 'Large Cap'},
        {'ticker': 'CME', 'company': 'CME Group Inc.', 'source': 'Large Cap'},
        {'ticker': 'TGT', 'company': 'Target Corporation', 'source': 'Large Cap'},
        {'ticker': 'REGN', 'company': 'Regeneron Pharmaceuticals Inc.', 'source': 'Large Cap'},
        {'ticker': 'APD', 'company': 'Air Products and Chemicals Inc.', 'source': 'Large Cap'},
        {'ticker': 'EOG', 'company': 'EOG Resources Inc.', 'source': 'Large Cap'},
        {'ticker': 'NSC', 'company': 'Norfolk Southern Corporation', 'source': 'Large Cap'},
        {'ticker': 'KLAC', 'company': 'KLA Corporation', 'source': 'Large Cap'},
        {'ticker': 'SLB', 'company': 'Schlumberger Limited', 'source': 'Large Cap'},
        {'ticker': 'MDLZ', 'company': 'Mondelez International Inc.', 'source': 'Large Cap'},
        {'ticker': 'ADI', 'company': 'Analog Devices Inc.', 'source': 'Large Cap'},
        {'ticker': 'ISRG', 'company': 'Intuitive Surgical Inc.', 'source': 'Large Cap'},
        {'ticker': 'CI', 'company': 'Cigna Corporation', 'source': 'Large Cap'},
        {'ticker': 'CMG', 'company': 'Chipotle Mexican Grill Inc.', 'source': 'Large Cap'},
        {'ticker': 'FISV', 'company': 'Fiserv Inc.', 'source': 'Large Cap'},
        {'ticker': 'TFC', 'company': 'Truist Financial Corporation', 'source': 'Large Cap'},
        {'ticker': 'MCD', 'company': 'McDonald\'s Corporation', 'source': 'Large Cap'},
        {'ticker': 'CVS', 'company': 'CVS Health Corporation', 'source': 'Large Cap'},
        {'ticker': 'EMR', 'company': 'Emerson Electric Co.', 'source': 'Large Cap'},
        {'ticker': 'BSX', 'company': 'Boston Scientific Corporation', 'source': 'Large Cap'},
        {'ticker': 'ITW', 'company': 'Illinois Tool Works Inc.', 'source': 'Large Cap'},
        {'ticker': 'WM', 'company': 'Waste Management Inc.', 'source': 'Large Cap'},
        {'ticker': 'GD', 'company': 'General Dynamics Corporation', 'source': 'Large Cap'},
        {'ticker': 'MCO', 'company': 'Moody\'s Corporation', 'source': 'Large Cap'},
        {'ticker': 'FDX', 'company': 'FedEx Corporation', 'source': 'Large Cap'},
        {'ticker': 'NOC', 'company': 'Northrop Grumman Corporation', 'source': 'Large Cap'},
        {'ticker': 'EQIX', 'company': 'Equinix Inc.', 'source': 'Large Cap'},
        {'ticker': 'APH', 'company': 'Amphenol Corporation', 'source': 'Large Cap'},
        {'ticker': 'ECL', 'company': 'Ecolab Inc.', 'source': 'Large Cap'},
        {'ticker': 'PSA', 'company': 'Public Storage', 'source': 'Large Cap'},
        {'ticker': 'AON', 'company': 'Aon plc', 'source': 'Large Cap'},
        {'ticker': 'CL', 'company': 'Colgate-Palmolive Company', 'source': 'Large Cap'},
        {'ticker': 'WELL', 'company': 'Welltower Inc.', 'source': 'Large Cap'},
        {'ticker': 'PLD', 'company': 'Prologis Inc.', 'source': 'Large Cap'},
        {'ticker': 'EL', 'company': 'Estee Lauder Companies Inc.', 'source': 'Large Cap'},
        {'ticker': 'MCHP', 'company': 'Microchip Technology Inc.', 'source': 'Large Cap'},
        {'ticker': 'HUM', 'company': 'Humana Inc.', 'source': 'Large Cap'},
        {'ticker': 'CTAS', 'company': 'Cintas Corporation', 'source': 'Large Cap'},
        {'ticker': 'FAST', 'company': 'Fastenal Company', 'source': 'Large Cap'},
        {'ticker': 'PAYX', 'company': 'Paychex Inc.', 'source': 'Large Cap'},
        {'ticker': 'ROST', 'company': 'Ross Stores Inc.', 'source': 'Large Cap'},
        {'ticker': 'ODFL', 'company': 'Old Dominion Freight Line Inc.', 'source': 'Large Cap'},
        {'ticker': 'VRSK', 'company': 'Verisk Analytics Inc.', 'source': 'Large Cap'},
        {'ticker': 'EXC', 'company': 'Exelon Corporation', 'source': 'Large Cap'},
        {'ticker': 'KMB', 'company': 'Kimberly-Clark Corporation', 'source': 'Large Cap'},
        {'ticker': 'CTSH', 'company': 'Cognizant Technology Solutions Corp.', 'source': 'Large Cap'},
        {'ticker': 'GWW', 'company': 'W.W. Grainger Inc.', 'source': 'Large Cap'},
        {'ticker': 'IDXX', 'company': 'IDEXX Laboratories Inc.', 'source': 'Large Cap'},
        {'ticker': 'YUM', 'company': 'Yum! Brands Inc.', 'source': 'Large Cap'},
        {'ticker': 'BIIB', 'company': 'Biogen Inc.', 'source': 'Large Cap'},
        {'ticker': 'KHC', 'company': 'Kraft Heinz Company', 'source': 'Large Cap'},
        {'ticker': 'DXCM', 'company': 'DexCom Inc.', 'source': 'Large Cap'},
        {'ticker': 'EA', 'company': 'Electronic Arts Inc.', 'source': 'Large Cap'},
        {'ticker': 'SBUX', 'company': 'Starbucks Corporation', 'source': 'Large Cap'},
        {'ticker': 'MNST', 'company': 'Monster Beverage Corporation', 'source': 'Large Cap'},
        {'ticker': 'EW', 'company': 'Edwards Lifesciences Corporation', 'source': 'Large Cap'},
        {'ticker': 'ILMN', 'company': 'Illumina Inc.', 'source': 'Large Cap'},
        {'ticker': 'WBA', 'company': 'Walgreens Boots Alliance Inc.', 'source': 'Large Cap'},
        {'ticker': 'CSGP', 'company': 'CoStar Group Inc.', 'source': 'Large Cap'},
        {'ticker': 'ANSS', 'company': 'ANSYS Inc.', 'source': 'Large Cap'},
        {'ticker': 'ZBH', 'company': 'Zimmer Biomet Holdings Inc.', 'source': 'Large Cap'},
        {'ticker': 'CPRT', 'company': 'Copart Inc.', 'source': 'Large Cap'},
        {'ticker': 'MKTX', 'company': 'MarketAxess Holdings Inc.', 'source': 'Large Cap'},
        {'ticker': 'WLTW', 'company': 'Willis Towers Watson Public Limited Company', 'source': 'Large Cap'},
        {'ticker': 'CDNS', 'company': 'Cadence Design Systems Inc.', 'source': 'Large Cap'},
        {'ticker': 'SNPS', 'company': 'Synopsys Inc.', 'source': 'Large Cap'},
        {'ticker': 'MAR', 'company': 'Marriott International Inc.', 'source': 'Large Cap'},
        {'ticker': 'ROP', 'company': 'Roper Technologies Inc.', 'source': 'Large Cap'},
        {'ticker': 'FTNT', 'company': 'Fortinet Inc.', 'source': 'Large Cap'},
        {'ticker': 'ADSK', 'company': 'Autodesk Inc.', 'source': 'Large Cap'},
        {'ticker': 'A', 'company': 'Agilent Technologies Inc.', 'source': 'Large Cap'},
        {'ticker': 'MSCI', 'company': 'MSCI Inc.', 'source': 'Large Cap'},
        {'ticker': 'EXR', 'company': 'Extended Stay America Inc.', 'source': 'Large Cap'},
        {'ticker': 'PCAR', 'company': 'PACCAR Inc.', 'source': 'Large Cap'},
        {'ticker': 'CMI', 'company': 'Cummins Inc.', 'source': 'Large Cap'},
        {'ticker': 'NXPI', 'company': 'NXP Semiconductors N.V.', 'source': 'Large Cap'},
        {'ticker': 'ORLY', 'company': 'O\'Reilly Automotive Inc.', 'source': 'Large Cap'},
        {'ticker': 'AZO', 'company': 'AutoZone Inc.', 'source': 'Large Cap'},
        {'ticker': 'DLTR', 'company': 'Dollar Tree Inc.', 'source': 'Large Cap'},
        {'ticker': 'EBAY', 'company': 'eBay Inc.', 'source': 'Large Cap'},
        {'ticker': 'CHTR', 'company': 'Charter Communications Inc.', 'source': 'Large Cap'},
        {'ticker': 'XLNX', 'company': 'Xilinx Inc.', 'source': 'Large Cap'},
        {'ticker': 'ALGN', 'company': 'Align Technology Inc.', 'source': 'Large Cap'},
        {'ticker': 'MXIM', 'company': 'Maxim Integrated Products Inc.', 'source': 'Large Cap'},
        {'ticker': 'SWKS', 'company': 'Skyworks Solutions Inc.', 'source': 'Large Cap'},
        {'ticker': 'INCY', 'company': 'Incyte Corporation', 'source': 'Large Cap'},
        {'ticker': 'SIRI', 'company': 'Sirius XM Holdings Inc.', 'source': 'Large Cap'},
        {'ticker': 'WDC', 'company': 'Western Digital Corporation', 'source': 'Large Cap'},
        {'ticker': 'NTAP', 'company': 'NetApp Inc.', 'source': 'Large Cap'},
        {'ticker': 'VIAC', 'company': 'ViacomCBS Inc.', 'source': 'Large Cap'},
        {'ticker': 'DISH', 'company': 'DISH Network Corporation', 'source': 'Large Cap'},
        {'ticker': 'FOXA', 'company': 'Fox Corporation Class A', 'source': 'Large Cap'},
        {'ticker': 'FOX', 'company': 'Fox Corporation Class B', 'source': 'Large Cap'},
        
        {'ticker': 'GME', 'company': 'GameStop Corp.', 'source': 'Popular'},
        {'ticker': 'AMC', 'company': 'AMC Entertainment Holdings Inc.', 'source': 'Popular'},
        {'ticker': 'PLTR', 'company': 'Palantir Technologies Inc.', 'source': 'Popular'},
        {'ticker': 'BB', 'company': 'BlackBerry Limited', 'source': 'Popular'},
        {'ticker': 'NOK', 'company': 'Nokia Corporation', 'source': 'Popular'},
        {'ticker': 'COIN', 'company': 'Coinbase Global Inc.', 'source': 'Crypto'},
        {'ticker': 'HOOD', 'company': 'Robinhood Markets Inc.', 'source': 'Popular'},
        {'ticker': 'RBLX', 'company': 'Roblox Corporation', 'source': 'Popular'},
        {'ticker': 'SNOW', 'company': 'Snowflake Inc.', 'source': 'Popular'},
        {'ticker': 'MSTR', 'company': 'MicroStrategy Incorporated', 'source': 'Crypto'},
        {'ticker': 'RIOT', 'company': 'Riot Platforms Inc.', 'source': 'Crypto'},
        {'ticker': 'MARA', 'company': 'Marathon Digital Holdings Inc.', 'source': 'Crypto'},
        {'ticker': 'TSM', 'company': 'Taiwan Semiconductor Manufacturing Co.', 'source': 'International'},
        {'ticker': 'ASML', 'company': 'ASML Holding N.V.', 'source': 'International'},
        {'ticker': 'NVO', 'company': 'Novo Nordisk A/S', 'source': 'International'},
        {'ticker': 'SHOP', 'company': 'Shopify Inc.', 'source': 'Growth'},
        {'ticker': 'SQ', 'company': 'Block Inc.', 'source': 'Growth'},
        {'ticker': 'ROKU', 'company': 'Roku Inc.', 'source': 'Growth'},
        {'ticker': 'PINS', 'company': 'Pinterest Inc.', 'source': 'Growth'},
        {'ticker': 'SNAP', 'company': 'Snap Inc.', 'source': 'Growth'},
        {'ticker': 'TWTR', 'company': 'Twitter Inc.', 'source': 'Growth'},
        {'ticker': 'UBER', 'company': 'Uber Technologies Inc.', 'source': 'Growth'},
        {'ticker': 'LYFT', 'company': 'Lyft Inc.', 'source': 'Growth'},
        {'ticker': 'ABNB', 'company': 'Airbnb Inc.', 'source': 'Growth'},
        {'ticker': 'DASH', 'company': 'DoorDash Inc.', 'source': 'Growth'},
        {'ticker': 'ZM', 'company': 'Zoom Video Communications Inc.', 'source': 'Growth'},
        {'ticker': 'PTON', 'company': 'Peloton Interactive Inc.', 'source': 'Growth'},
        {'ticker': 'DOCU', 'company': 'DocuSign Inc.', 'source': 'Growth'},
        {'ticker': 'CRWD', 'company': 'CrowdStrike Holdings Inc.', 'source': 'Growth'},
        {'ticker': 'OKTA', 'company': 'Okta Inc.', 'source': 'Growth'},
        {'ticker': 'DDOG', 'company': 'Datadog Inc.', 'source': 'Growth'},
        {'ticker': 'NET', 'company': 'Cloudflare Inc.', 'source': 'Growth'},
        {'ticker': 'TWLO', 'company': 'Twilio Inc.', 'source': 'Growth'},
        {'ticker': 'SPLK', 'company': 'Splunk Inc.', 'source': 'Growth'},
        {'ticker': 'WDAY', 'company': 'Workday Inc.', 'source': 'Growth'},
        {'ticker': 'VEEV', 'company': 'Veeva Systems Inc.', 'source': 'Growth'},
        {'ticker': 'ZS', 'company': 'Zscaler Inc.', 'source': 'Growth'},
        {'ticker': 'PANW', 'company': 'Palo Alto Networks Inc.', 'source': 'Growth'},
        {'ticker': 'TEAM', 'company': 'Atlassian Corporation Plc', 'source': 'Growth'},
        {'ticker': 'MDB', 'company': 'MongoDB Inc.', 'source': 'Growth'},
        {'ticker': 'ESTC', 'company': 'Elastic N.V.', 'source': 'Growth'},
        {'ticker': 'FSLY', 'company': 'Fastly Inc.', 'source': 'Growth'},
        {'ticker': 'FVRR', 'company': 'Fiverr International Ltd.', 'source': 'Growth'},
        {'ticker': 'UPWK', 'company': 'Upwork Inc.', 'source': 'Growth'},
        {'ticker': 'ETSY', 'company': 'Etsy Inc.', 'source': 'Growth'},
        {'ticker': 'SPOT', 'company': 'Spotify Technology S.A.', 'source': 'Growth'},
        {'ticker': 'NFLX', 'company': 'Netflix Inc.', 'source': 'Growth'},
        {'ticker': 'DIS', 'company': 'Walt Disney Company', 'source': 'Growth'},
        {'ticker': 'BABA', 'company': 'Alibaba Group Holding Limited', 'source': 'International'},
        {'ticker': 'JD', 'company': 'JD.com Inc.', 'source': 'International'},
        {'ticker': 'PDD', 'company': 'PDD Holdings Inc.', 'source': 'International'},
        {'ticker': 'NIO', 'company': 'NIO Inc.', 'source': 'International'},
        {'ticker': 'XPEV', 'company': 'XPeng Inc.', 'source': 'International'},
        {'ticker': 'LI', 'company': 'Li Auto Inc.', 'source': 'International'}
    ]
    
    print(f"Compiled {len(top_200_stocks)} stocks for top 200 list")
    return top_200_stocks

def get_additional_large_cap_tickers() -> List[Dict[str, str]]:
    """Add additional large-cap stocks that might not be in S&P 500"""
    additional_tickers = [
        {'ticker': 'BRK.A', 'company': 'Berkshire Hathaway Class A', 'source': 'Large Cap'},
        {'ticker': 'BRK.B', 'company': 'Berkshire Hathaway Class B', 'source': 'Large Cap'},
        
        {'ticker': 'TSM', 'company': 'Taiwan Semiconductor', 'source': 'Large Cap'},
        {'ticker': 'ASML', 'company': 'ASML Holding', 'source': 'Large Cap'},
        {'ticker': 'NVO', 'company': 'Novo Nordisk', 'source': 'Large Cap'},
        
        {'ticker': 'GME', 'company': 'GameStop', 'source': 'Popular'},
        {'ticker': 'AMC', 'company': 'AMC Entertainment', 'source': 'Popular'},
        {'ticker': 'BB', 'company': 'BlackBerry', 'source': 'Popular'},
        {'ticker': 'NOK', 'company': 'Nokia', 'source': 'Popular'},
        
        {'ticker': 'COIN', 'company': 'Coinbase', 'source': 'Crypto'},
        {'ticker': 'MSTR', 'company': 'MicroStrategy', 'source': 'Crypto'},
        {'ticker': 'RIOT', 'company': 'Riot Platforms', 'source': 'Crypto'},
        {'ticker': 'MARA', 'company': 'Marathon Digital', 'source': 'Crypto'},
        
        {'ticker': 'PLTR', 'company': 'Palantir', 'source': 'Popular'},
        {'ticker': 'SNOW', 'company': 'Snowflake', 'source': 'Popular'},
        {'ticker': 'RBLX', 'company': 'Roblox', 'source': 'Popular'},
        {'ticker': 'HOOD', 'company': 'Robinhood', 'source': 'Popular'},
    ]
    
    print(f"Added {len(additional_tickers)} additional large-cap/popular tickers")
    return additional_tickers

def compile_top_200_list() -> List[Dict[str, str]]:
    """Compile the top 200 stocks by combining S&P 500 and additional stocks"""
    print("Compiling top 200 stocks list...")
    
    sp500_tickers = extract_sp500_tickers()
    
    additional_tickers = get_additional_large_cap_tickers()
    
    all_tickers = {}
    
    for ticker_info in sp500_tickers:
        ticker = ticker_info['ticker']
        all_tickers[ticker] = ticker_info
    
    for ticker_info in additional_tickers:
        ticker = ticker_info['ticker']
        if ticker not in all_tickers:
            all_tickers[ticker] = ticker_info
    
    ticker_list = list(all_tickers.values())
    top_200 = ticker_list[:200]
    
    print(f"Compiled {len(top_200)} tickers for top 200 list")
    return top_200

def save_ticker_data(tickers: List[Dict[str, str]], filename: str):
    """Save ticker data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(tickers, f, indent=2)
    print(f"Saved ticker data to {filename}")

def generate_ticker_sets(tickers: List[Dict[str, str]]) -> Tuple[str, str]:
    """Generate Python code for ticker sets"""
    
    ticker_symbols = [t['ticker'] for t in tickers]
    
    common_tickers_code = "common_tickers = {\n"
    for i, ticker in enumerate(sorted(ticker_symbols)):
        if i % 10 == 0:
            common_tickers_code += "    "
        common_tickers_code += f'"{ticker}", '
        if (i + 1) % 10 == 0:
            common_tickers_code += "\n"
    
    if len(ticker_symbols) % 10 != 0:
        common_tickers_code += "\n"
    common_tickers_code += "}"
    
    mock_data_code = """# Generate mock data for all top 200 tickers
        base_mentions = {
            'AAPL': 2500, 'MSFT': 2200, 'GOOGL': 2000, 'GOOG': 2000, 'AMZN': 1900,
            'NVDA': 2800, 'TSLA': 3000, 'META': 1800, 'BRK.B': 1200, 'BRK.A': 800,
            
            'V': 1000, 'JPM': 1100, 'JNJ': 900, 'WMT': 800, 'PG': 700,
            'UNH': 900, 'HD': 800, 'MA': 950, 'BAC': 1200, 'XOM': 1100,
            
            'GME': 2500, 'AMC': 2000, 'PLTR': 1500, 'BB': 1200, 'NOK': 1000,
            'COIN': 1800, 'HOOD': 1400, 'RBLX': 1300, 'SNOW': 1100,
        }
        
        for ticker_info in ["""
    
    for ticker in tickers:
        mock_data_code += f'\n            {{"ticker": "{ticker["ticker"]}", "company": "{ticker["company"]}"}},'
    
    mock_data_code += """
        ]:
            ticker = ticker_info["ticker"]
            
            if ticker in base_mentions:
                base_count = base_mentions[ticker]
            else:
                base_count = max(200, 1000 - (len(self.mention_data) * 3))
            
            for i in range(30):
                date = (datetime.now() - timedelta(days=29-i)).strftime('%Y-%m-%d')
                
                volatility = random.uniform(0.7, 1.3)
                daily_mentions = int(base_count * volatility)
                
                weekday = (datetime.now() - timedelta(days=29-i)).weekday()
                if weekday >= 5:  # Saturday, Sunday
                    daily_mentions = int(daily_mentions * 0.6)
                
                if date not in self.mention_data:
                    self.mention_data[date] = {}
                
                self.mention_data[date][ticker] = daily_mentions"""
    
    return common_tickers_code, mock_data_code

def main():
    print("=" * 60)
    print("RESEARCHING TOP 200 STOCKS BY MARKET CAP")
    print("=" * 60)
    
    top_200_tickers = compile_top_200_list()
    
    save_ticker_data(top_200_tickers, '/home/ubuntu/repos/reddit-wisdom/top_200_stocks.json')
    
    common_tickers_code, mock_data_code = generate_ticker_sets(top_200_tickers)
    
    with open('/home/ubuntu/repos/reddit-wisdom/generated_ticker_code.py', 'w') as f:
        f.write("# Generated ticker validation code\n\n")
        f.write(common_tickers_code)
        f.write("\n\n# Generated mock data code\n\n")
        f.write(mock_data_code)
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"✅ Compiled {len(top_200_tickers)} tickers for top 200 list")
    print(f"✅ Saved ticker data to top_200_stocks.json")
    print(f"✅ Generated code snippets in generated_ticker_code.py")
    
    print(f"\nFirst 20 tickers:")
    for i, ticker in enumerate(top_200_tickers[:20]):
        print(f"  {i+1:2d}. {ticker['ticker']:6s} - {ticker['company']}")
    
    print(f"\n... and {len(top_200_tickers) - 20} more tickers")
    
    return top_200_tickers

if __name__ == "__main__":
    main()
