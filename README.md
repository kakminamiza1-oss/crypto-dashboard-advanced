# Momentum Desk — Binance Futures Scanner

Static, browser-based scanner for Binance USDT-M perpetual markets. Uses Binance public REST data; no API key or order execution is involved.

## Run locally

From the repository root, start a static web server (opening `index.html` directly may be blocked by browser network/CORS policy):

```powershell
py -m http.server 8080
```

Open <http://127.0.0.1:8080>.

## Features

- Selects the top 10/20/30 USDT perpetual pairs by 24-hour quote volume.
- Fetches closed 5m, 15m and 1h candles and calculates EMA alignment, RSI, MACD histogram, ATR, relative volume and a simple breakout/candle-quality check.
- Ranks candidates with a transparent heuristic score and displays price, 24h volume/change, spread and an ATR-based reference plan.
- Filters by direction, score and volume surge; exports the scan as CSV.
- Browser-only frontend. Binance public endpoints are used directly; network access, Binance availability, API limits and browser connectivity can affect results.

## Scoring and safety notes

The score is an unvalidated research heuristic, not a probability of success. LONG/SHORT is shown only when all three timeframe trends align and momentum, volume and candle checks pass; otherwise the row is marked “รอยืนยัน”. The displayed Entry/SL/TP is an illustrative ATR-based reference, not an order instruction. This project does not place trades and must not be treated as financial advice. Backtest and paper-trade before relying on any screening rule.
