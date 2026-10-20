# GoldSniper 3R — project scaffold

**Target:** Android-controlled XAUUSD MT5 Expert Advisor, first broker FTMO, prop-challenge mode, fully automatic, configurable 1% risk and default 1:3 R:R.

## Status (honest build ledger)

- **Implemented in this source package:** MQL5 EA source, Android UI starter, HTTPS API contract/backend starter, GitHub Actions Android build workflow, setup instructions.
- **Compiled:** Not yet. This environment does not include MetaEditor/MT5 or an Android SDK verification run.
- **Tested:** Not yet. No Strategy Tester or demo-account results are claimed.
- **Deployed:** Not deployed. No VPS, backend, domain, GitHub repository, or FTMO credentials have been provisioned.
- **APK:** Not included as a prebuilt binary. Use the Android-only GitHub Actions workflow to build an APK in the cloud.

This is a starting project, not a guarantee of profitability or FTMO-rule compliance. Run demo tests first. Confirm the exact FTMO account type, instrument symbol, contract specification, EA and automated-trading rules before a challenge.

## Project layout

- `mt5/GoldSniper3R.mq5` — EA source.
- `android/` — native Android app starter (Kotlin/Jetpack Compose).
- `backend/` — minimal FastAPI command/status relay starter; deploy behind HTTPS and authentication before use.
- `.github/workflows/android-apk.yml` — cloud APK build workflow.
- `docs/ANDROID_ONLY_BUILD.md` — phone-only build and install instructions.
- `docs/SECURITY_AND_DEPLOYMENT.md` — deployment and security checklist.

## Trading model

1. M15 reference levels: previous-day high/low and Asian session high/low.
2. M5 sweep/reclaim followed by displacement and a close beyond a recent confirmed swing.
3. Entry on retracement into the displacement-created FVG.
4. Stop beyond sweep extreme; TP at 3R.
5. Position size estimated from equity risk and broker tick-value metadata, rounded down to symbol volume steps.
6. Daily loss guard, daily trade limit, spread guard, one position per symbol/magic, session filter, and no martingale/grid.

The EA's objective checks are intentionally conservative. It may take few trades. It does not predict or guarantee a win rate. A market order is sent after the FVG retest is detected; no pending limit order is left behind.

## Before live use

- Compile in MetaEditor and fix any broker/build-specific diagnostics.
- Verify symbol suffixes (for example, `XAUUSD` vs `XAUUSD.`) and contract metadata.
- Backtest with real ticks, variable spreads, commissions and slippage; use out-of-sample testing.
- Forward-test on a demo account.
- Confirm FTMO's current EA, news-trading, risk and account-specific restrictions. The EA's local daily loss guard is not a substitute for firm-level drawdown rules.
- Do not put broker passwords, API secrets or account credentials in this repository.
