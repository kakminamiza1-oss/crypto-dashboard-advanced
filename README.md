# Momentum Desk — Binance Futures Scanner

Static browser dashboard for scanning Binance USDT-M perpetual markets. Uses public market-data REST endpoints and market ticker WebSocket only; no API key and no order execution.

## Run locally

From the repository root, serve the static page (recommended instead of opening the file directly):

```powershell
py -m http.server 8080
```

Open <http://127.0.0.1:8080>.

## Included

- Top 10/20/30 USDT perpetual pairs ranked by 24-hour quote volume.
- Closed-candle 5m/15m/1h EMA20/EMA50 trend alignment, RSI, MACD histogram, ATR, relative volume, breakout and candle-close quality checks.
- Liquidity screen using top-of-book spread; candidates are withheld unless timeframe trend, momentum, relative volume, candle quality and spread gates align.
- Score-ranked LONG / SHORT / WAIT scan, filters, CSV export and ATR-based reference levels.
- Live ticker updates over Binance Futures WebSocket and optional 60-second full scan refresh.
- Responsive dark dashboard and market breadth summary.

## Notes

The score is an unvalidated heuristic, not a probability of success. All signal-like labels are for research and screening only. Entry/SL/TP are illustrative ATR-based reference levels, not order instructions or investment advice. The page depends on internet access, Binance public endpoint availability, browser connectivity and exchange rate limits. Backtest and paper-trade rules before relying on them. Never add exchange trading credentials to this static dashboard.
