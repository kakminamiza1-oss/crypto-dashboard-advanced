# Momentum Desk — Binance Futures Scanner

Static browser dashboard for scanning Binance USDT-M perpetual markets. Uses public market-data REST endpoints and market ticker WebSocket only; no API key and no order execution.

## Run locally

Python 3 is required; the dashboard has no third-party package dependencies.

### Windows

Double-click `run.bat`. It starts the local server, picks an available port from `8080` through `8090`, and opens the dashboard in your default browser. Keep the terminal window open while using the dashboard; press Ctrl+C or close that window to stop the server.

### macOS / Linux

From the repository root, run:

```sh
python3 run_local.py
```

The script opens the dashboard automatically and prints its local URL. If you prefer Python's basic static server, you can also run:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Then open <http://127.0.0.1:8080>.

The local server listens only on `127.0.0.1` and serves the dashboard at `/` or `/index.html`; `/health` is available for a basic server check. Do not open `index.html` directly as a `file://` URL. Internet access is still required for Binance market-data REST and WebSocket connections.

## Troubleshooting

- **No available port:** the launcher tries ports 8080–8090. Stop another local server in that range and try again.
- **Page opens but market data does not load:** the local server is working, but the browser still needs internet access to `fapi.binance.com` and `fstream.binance.com`. Check your network/region, browser developer console, and Binance rate-limit responses.
- **Python is not recognized on Windows:** install Python 3 from <https://www.python.org/downloads/windows/> and enable the Python launcher, then run `run.bat` again.

## Included

- Top 10/20/30 USDT perpetual pairs ranked by 24-hour quote volume.
- Closed-candle 5m/15m/1h EMA20/EMA50 trend alignment, RSI, MACD histogram, ATR, relative volume, breakout and candle-close quality checks.
- Liquidity screen using top-of-book spread; candidates are withheld unless timeframe trend, momentum, relative volume, candle quality and spread gates align.
- Score-ranked LONG / SHORT / WAIT scan, filters, CSV export and ATR-based reference levels.
- Live ticker updates over Binance Futures WebSocket and optional 60-second full scan refresh.
- Responsive dark dashboard and market breadth summary.

## Notes

The score is an unvalidated heuristic, not a probability of success. All signal-like labels are for research and screening only. Entry/SL/TP are illustrative ATR-based reference levels, not order instructions or investment advice. The page depends on internet access, Binance public endpoint availability, browser connectivity and exchange rate limits. Backtest and paper-trade rules before relying on them. Never add exchange trading credentials to this static dashboard.
