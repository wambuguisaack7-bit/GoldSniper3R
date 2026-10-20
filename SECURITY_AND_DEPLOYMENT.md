# Security and deployment

## Required production architecture

Android app (HTTPS) -> authenticated API -> durable command/status store -> EA polling the API -> FTMO MT5 terminal on Windows VPS.

The included backend is a development starter, not production-ready. Before live trading:
- Deploy only behind HTTPS.
- Set a long random `API_TOKEN` secret in the server environment and matching token in the EA/app configuration.
- Add per-account authorization, rate limiting, audit logs, durable storage, request signing/replay protection, and safe command expiry.
- Never accept arbitrary shell commands or MQL code from the API.
- Do not store FTMO passwords in the Android app or source repository.
- Treat remote close-all as a high-impact action and require explicit confirmation in the UI.
- Keep risk controls enforced locally in the EA; remote settings must not override the hard risk ceiling.
- Make the EA fail-safe: if connectivity is lost, it should stop accepting remote commands and continue managing existing broker-side SL/TP.

## Important implementation gap

The initial EA and Android starter are not yet connected end-to-end. The backend includes basic status/command endpoints, but the EA has not been given a production HTTP bridge in this scaffold. This avoids pretending a nonfunctional link is deployed. The next implementation stage is to add authenticated `WebRequest` polling and signed command handling to the EA, then test on a dedicated demo terminal.

## FTMO / prop-firm caution

Rules differ by product and may change. Confirm current FTMO terms for the exact account type, EA automation, prohibited practices, news restrictions and drawdown methodology. The EA cannot guarantee compliance or successful passing.
