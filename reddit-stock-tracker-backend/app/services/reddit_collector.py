from pmaw import PushshiftAPI
from datetime import datetime, timedelta
from typing import List, Dict


class RedditCollector:
    def __init__(self):
        self.api = PushshiftAPI(num_workers=10, rate_limit=60)
        self.subreddits = ["wallstreetbets", "stocks", "investing", "SecurityAnalysis"]

    def collect_recent_data(self, days_back: int = 30) -> List[Dict]:
        """Collect submissions and comments from the last N days"""
        end_time = int(datetime.now().timestamp())
        start_time = int((datetime.now() - timedelta(days=days_back)).timestamp())

        all_data = []

        for subreddit in self.subreddits:
            try:
                print(f"Collecting data from r/{subreddit}...")

                submissions = self.api.search_submissions(
                    subreddit=subreddit, after=start_time, before=end_time, limit=1000
                )

                comments = self.api.search_comments(
                    subreddit=subreddit, after=start_time, before=end_time, limit=5000
                )

                all_data.extend([item for item in submissions])
                all_data.extend([item for item in comments])

                submission_count = len([item for item in submissions])
                comment_count = len([item for item in comments])
                print(
                    f"Collected {submission_count} submissions and "
                    f"{comment_count} comments from r/{subreddit}"
                )

            except Exception as e:
                print(f"Error collecting from r/{subreddit}: {e}")
                continue

        print(f"Total collected: {len(all_data)} items")
        return all_data
