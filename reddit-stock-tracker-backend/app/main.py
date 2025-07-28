from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from .services.reddit_collector import RedditCollector
from .services.ticker_extractor import TickerExtractor
from .services.data_processor import DataProcessor

load_dotenv()

app = FastAPI(title="Reddit Stock Trend Tracker")

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

reddit_collector = RedditCollector()
ticker_extractor = TickerExtractor()
data_processor = DataProcessor()


class TickerRequest(BaseModel):
    ticker: str


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/api/trending")
async def get_trending_tickers(limit: int = 10):
    """Get top trending stock tickers"""
    trending = data_processor.get_trending_tickers(limit)
    return {"trending_tickers": trending}


@app.get("/api/ticker/{ticker}/history")
async def get_ticker_history(ticker: str):
    """Get mention history for a specific ticker"""
    history = data_processor.get_ticker_history(ticker)
    return {"ticker": ticker.upper(), "history": history}


@app.post("/api/ticker/validate")
async def validate_ticker(request: TickerRequest):
    """Validate a custom ticker"""
    is_valid = ticker_extractor.validate_ticker(request.ticker.upper())
    return {"ticker": request.ticker.upper(), "valid": is_valid}


@app.get("/api/data/refresh")
async def refresh_data():
    """Manually refresh Reddit data"""
    try:
        print("Starting data refresh...")
        reddit_data = reddit_collector.collect_recent_data(30)
        data_processor.process_reddit_data(reddit_data, ticker_extractor)
        trending = data_processor.get_trending_tickers(10)
        return {
            "status": "success",
            "items_processed": len(reddit_data),
            "trending_count": len(trending),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error refreshing data: {str(e)}")


@app.on_event("startup")
async def startup_event():
    """Collect initial data on startup"""
    try:
        print("Collecting Reddit data on startup...")
        reddit_data = reddit_collector.collect_recent_data(30)
        data_processor.process_reddit_data(reddit_data, ticker_extractor)
        print(f"Processed {len(reddit_data)} Reddit items")
    except Exception as e:
        print(f"Error during startup data collection: {e}")
