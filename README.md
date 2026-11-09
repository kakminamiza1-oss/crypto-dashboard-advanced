# Momentum Desk — Binance Futures Scanner

Static browser dashboard for scanning Binance USDT-M perpetual markets. Uses public market-data REST endpoints and market ticker WebSocket only; no API key and no order execution.

## Run locally

### Windows

1. Install Python 3 if it is not already installed.
2. Double-click `run.bat`. It starts a local web server and opens the dashboard at <http://127.0.0.1:8080>.
3. Keep the server window open while using the dashboard. Close that window to stop it.

Alternatively, from the repository root in PowerShell:

```powershell
py -m http.server 8080 --bind 127.0.0.1
```

Then open <http://127.0.0.1:8080>.

### macOS / Linux

From the repository root, run:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Then open <http://127.0.0.1:8080>.

Do not open `index.html` directly as a `file://` URL; use the local server. The dashboard needs internet access to reach Binance public market-data endpoints and WebSocket.

## Troubleshooting

- **Port 8080 is already in use:** stop the other server, or run `py -m http.server 8081 --bind 127.0.0.1` and open <http://127.0.0.1:8081>.
- **Market data does not load:** check internet access and whether your network or region blocks Binance Futures (`fapi.binance.com` / `fstream.binance.com`). Retry after a short wait if Binance is rate-limiting requests.
- **Python is not recognized on Windows:** install Python 3 and enable the Python launcher, then run `run.bat` again.

## Included

- Top 10/20/30 USDT perpetual pairs ranked by 24-hour quote volume.
- Closed-candle 5m/15m/1h EMA20/EMA50 trend alignment, RSI, MACD histogram, ATR, relative volume, breakout and candle-close quality checks.
- Liquidity screen using top-of-book spread; candidates are withheld unless timeframe trend, momentum, relative volume, candle quality and spread gates align.
- Score-ranked LONG / SHORT / WAIT scan, filters, CSV export and ATR-based reference levels.
- Live ticker updates over Binance Futures WebSocket and optional 60-second full scan refresh.
- Responsive dark dashboard and market breadth summary.

## Notes

The score is an unvalidated heuristic, not a probability of success. All signal-like labels are for research and screening only. Entry/SL/TP are illustrative ATR-based reference levels, not order instructions or investment advice. The page depends on internet access, Binance public endpoint availability, browser connectivity and exchange rate limits. Backtest and paper-trade rules before relying on them. Never add exchange trading credentials to this static dashboard.
