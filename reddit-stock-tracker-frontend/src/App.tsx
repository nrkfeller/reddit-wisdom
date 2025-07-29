import { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Search, TrendingUp, AlertCircle, RefreshCw } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Alert, AlertDescription } from '@/components/ui/alert';

interface TrendingTicker {
  ticker: string;
  total_mentions: number;
}

interface TickerHistory {
  date: string;
  mentions: number;
}

function App() {
  const [trendingTickers, setTrendingTickers] = useState<TrendingTicker[]>([]);
  const [selectedTickers, setSelectedTickers] = useState<string[]>([]);
  const [chartData, setChartData] = useState<any[]>([]);
  const [customTicker, setCustomTicker] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
  
  const getApiConfig = (): { baseUrl: string; headers: HeadersInit } => {
    try {
      const url = new URL(API_URL);
      if (url.username && url.password) {
        const credentials = btoa(`${url.username}:${url.password}`);
        const cleanUrl = `${url.protocol}//${url.host}`;
        return {
          baseUrl: cleanUrl,
          headers: { 'Authorization': `Basic ${credentials}` }
        };
      }
      return { baseUrl: API_URL, headers: {} };
    } catch {
      return { baseUrl: API_URL, headers: {} };
    }
  };
  
  const { baseUrl: API_BASE, headers: authHeaders } = getApiConfig();

  useEffect(() => {
    fetchTrendingTickers();
  }, []);

  const fetchTrendingTickers = async () => {
    try {
      setLoading(true);
      setError('');
      const response = await fetch(`${API_BASE}/api/trending`, {
        headers: authHeaders
      });
      const data = await response.json();
      setTrendingTickers(data.trending_tickers);
      
      const topTickers = data.trending_tickers.slice(0, 5).map((t: TrendingTicker) => t.ticker);
      setSelectedTickers(topTickers);
      await updateChartData(topTickers);
    } catch (err) {
      setError('Failed to fetch trending data');
      console.error('Error fetching trending data:', err);
    } finally {
      setLoading(false);
    }
  };

  const updateChartData = async (tickers: string[]) => {
    try {
      const historyPromises = tickers.map(ticker =>
        fetch(`${API_BASE}/api/ticker/${ticker}/history`, {
          headers: authHeaders
        }).then(r => r.json())
      );
      
      const histories = await Promise.all(historyPromises);
      
      const dateMap = new Map();
      histories.forEach(history => {
        history.history.forEach((point: TickerHistory) => {
          if (!dateMap.has(point.date)) {
            dateMap.set(point.date, { date: point.date });
          }
          dateMap.get(point.date)[history.ticker] = point.mentions;
        });
      });
      
      const chartData = Array.from(dateMap.values()).sort((a, b) => a.date.localeCompare(b.date));
      setChartData(chartData);
    } catch (err) {
      setError('Failed to fetch ticker history');
      console.error('Error fetching ticker history:', err);
    }
  };

  const addCustomTicker = async () => {
    if (!customTicker.trim()) return;
    
    try {
      setLoading(true);
      setError('');
      const response = await fetch(`${API_BASE}/api/ticker/validate`, {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          ...authHeaders
        },
        body: JSON.stringify({ ticker: customTicker.toUpperCase() })
      });
      
      const data = await response.json();
      if (data.valid) {
        const newTickers = [...selectedTickers, data.ticker];
        setSelectedTickers(newTickers);
        await updateChartData(newTickers);
        setCustomTicker('');
        setError('');
      } else {
        setError(`Invalid ticker: ${customTicker.toUpperCase()}`);
      }
    } catch (err) {
      setError('Failed to validate ticker');
      console.error('Error validating ticker:', err);
    } finally {
      setLoading(false);
    }
  };

  const removeTicker = (tickerToRemove: string) => {
    const newTickers = selectedTickers.filter(ticker => ticker !== tickerToRemove);
    setSelectedTickers(newTickers);
    updateChartData(newTickers);
  };

  const refreshData = async () => {
    try {
      setLoading(true);
      setError('');
      await fetch(`${API_BASE}/api/data/refresh`, {
        headers: authHeaders
      });
      await fetchTrendingTickers();
    } catch (err) {
      setError('Failed to refresh data');
      console.error('Error refreshing data:', err);
    } finally {
      setLoading(false);
    }
  };

  const getRandomColor = (index: number) => {
    const colors = [
      '#8884d8', '#82ca9d', '#ffc658', '#ff7300', '#00ff00',
      '#ff00ff', '#00ffff', '#ff0000', '#0000ff', '#ffff00'
    ];
    return colors[index % colors.length];
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        <header className="mb-8">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-4xl font-bold text-gray-900 mb-2">Reddit Stock Trend Tracker</h1>
              <p className="text-gray-600">Track trending stock mentions from Reddit communities</p>
            </div>
            <Button onClick={refreshData} disabled={loading} variant="outline">
              <RefreshCw className={`h-4 w-4 mr-2 ${loading ? 'animate-spin' : ''}`} />
              Refresh Data
            </Button>
          </div>
        </header>

        {error && (
          <Alert className="mb-6 border-red-200 bg-red-50">
            <AlertCircle className="h-4 w-4 text-red-600" />
            <AlertDescription className="text-red-800">{error}</AlertDescription>
          </Alert>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Trending Stocks Sidebar */}
          <div className="lg:col-span-1">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <TrendingUp className="h-5 w-5" />
                  Trending Stocks
                </CardTitle>
                <CardDescription>Currently charted stocks (click to remove)</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-2 max-h-96 overflow-y-auto">
                  {selectedTickers.map((ticker, index) => {
                    const trendingData = trendingTickers.find(t => t.ticker === ticker);
                    const mentions = trendingData ? trendingData.total_mentions : 'N/A';
                    return (
                      <div key={ticker} className="flex justify-between items-center p-2 rounded hover:bg-red-50 cursor-pointer group"
                           onClick={() => removeTicker(ticker)}>
                        <span className="font-medium">#{index + 1} ${ticker}</span>
                        <div className="flex items-center gap-2">
                          <span className="text-sm text-gray-600">{mentions} mentions</span>
                          <span className="text-red-500 opacity-0 group-hover:opacity-100 transition-opacity">×</span>
                        </div>
                      </div>
                    );
                  })}
                  {selectedTickers.length === 0 && (
                    <div className="text-center text-gray-500 py-4">
                      No stocks selected. Add a custom ticker below to get started.
                    </div>
                  )}
                </div>
                
                <div className="mt-6 space-y-2">
                  <label className="text-sm font-medium">Add Custom Ticker</label>
                  <div className="flex gap-2">
                    <Input
                      placeholder="Enter ticker (e.g., AAPL)"
                      value={customTicker}
                      onChange={(e) => setCustomTicker(e.target.value)}
                      onKeyPress={(e) => e.key === 'Enter' && addCustomTicker()}
                    />
                    <Button onClick={addCustomTicker} disabled={loading}>
                      <Search className="h-4 w-4" />
                    </Button>
                  </div>
                </div>

              </CardContent>
            </Card>
          </div>

          {/* Chart Area */}
          <div className="lg:col-span-2">
            <Card>
              <CardHeader>
                <CardTitle>Mention Trends</CardTitle>
                <CardDescription>Daily mention volume over the last month</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="h-96">
                  {chartData.length > 0 ? (
                    <ResponsiveContainer width="100%" height="100%">
                      <LineChart data={chartData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis 
                          dataKey="date" 
                          tick={{ fontSize: 12 }}
                          tickFormatter={(value) => new Date(value).toLocaleDateString()}
                        />
                        <YAxis />
                        <Tooltip 
                          labelFormatter={(value) => new Date(value).toLocaleDateString()}
                          formatter={(value, name) => [value, `$${name}`]}
                        />
                        <Legend />
                        {selectedTickers.map((ticker, index) => (
                          <Line
                            key={ticker}
                            type="monotone"
                            dataKey={ticker}
                            stroke={getRandomColor(index)}
                            strokeWidth={2}
                            dot={false}
                          />
                        ))}
                      </LineChart>
                    </ResponsiveContainer>
                  ) : (
                    <div className="flex items-center justify-center h-full text-gray-500">
                      {loading ? 'Loading chart data...' : 'Select tickers to view trends'}
                    </div>
                  )}
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
