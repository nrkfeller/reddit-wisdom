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
        """Initialize with mock data for development when no Reddit data is available"""
        from datetime import datetime, timedelta
        import random

        end_date = datetime.now().date()

        tickers = {
            "TSLA": {"base": 150, "volatility": 50},
            "GME": {"base": 120, "volatility": 80},
            "AAPL": {"base": 100, "volatility": 30},
            "AMC": {"base": 90, "volatility": 60},
            "NVDA": {"base": 80, "volatility": 40},
            "MSFT": {"base": 70, "volatility": 25},
            "GOOGL": {"base": 60, "volatility": 20},
            "GOOG": {"base": 58, "volatility": 18},
            "PLTR": {"base": 55, "volatility": 25},
            "META": {"base": 50, "volatility": 35},
            "AMD": {"base": 45, "volatility": 30},
        }

        for i in range(30):
            current_date = (end_date - timedelta(days=i)).isoformat()

            for ticker, config in tickers.items():
                base_mentions = config["base"]
                volatility = config["volatility"]

                day_of_week = (end_date - timedelta(days=i)).weekday()
                weekend_factor = 0.6 if day_of_week >= 5 else 1.0

                spike_factor = (
                    random.uniform(0.5, 2.0) if random.random() < 0.1 else 1.0
                )

                mentions = int(
                    base_mentions * weekend_factor * spike_factor
                    + random.randint(-volatility // 2, volatility // 2)
                )
                mentions = max(0, mentions)  # Ensure non-negative

                if mentions > 0:
                    self.mention_data[current_date][ticker] = mentions
