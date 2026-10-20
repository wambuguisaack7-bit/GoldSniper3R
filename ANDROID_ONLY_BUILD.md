# Build and install from Android only

You do not need to own a PC. You do need internet access and a GitHub account. GitHub Actions builds the Android APK on a cloud runner.

## A. Upload the project to GitHub using your phone

1. Download and extract `GoldSniper3R-project.zip` on your phone (Files app or an archive app).
2. Open GitHub in Chrome and create a **private** repository named `GoldSniper3R`.
3. Upload the **contents** of the extracted folder, not the ZIP itself. Ensure `.github/workflows/android-apk.yml` is present in the repository. GitHub's mobile upload interface may not show hidden `.github` files; if it cannot upload them, use GitHub's web editor to create `.github/workflows/android-apk.yml` and paste in the file contents from this project.
4. Commit the files to the default branch.

## B. Run the cloud build

1. In the repository, open **Actions**.
2. Enable workflows if GitHub asks.
3. Select **Build GoldSniper 3R Android APK** and tap **Run workflow** (or push a commit to trigger it).
4. Open the completed workflow run.
5. Under **Artifacts**, download `GoldSniper3R-debug-apk`.
6. Extract the downloaded artifact ZIP and locate `app-debug.apk`.

## C. Install

1. Tap `app-debug.apk` in your Android Files app.
2. If Android blocks it, allow installation from that source in the prompt/settings, then return to the installer.
3. Install and open GoldSniper 3R.

The starter Android app currently provides a dashboard/control UI scaffold. It does **not** yet have a production backend URL, deployed cloud service, authenticated MT5 bridge, or verified live command execution. The UI cannot place trades until the EA, backend and VPS are separately configured and connected.

## D. MT5 EA setup (requires Windows MT5/MetaEditor on a hosted machine)

1. Copy `mt5/GoldSniper3R.mq5` into the hosted machine's `MQL5/Experts/` folder.
2. Compile it with MetaEditor.
3. Attach it to the correct FTMO demo/challenge XAUUSD chart and enable Algo Trading.
4. Verify symbol name, lot limits, tick values, server time, session times and Journal logs.
5. Test only on demo before a challenge account.

The Android app build does not compile MQL5. MT5 EAs require MetaEditor/MT5 environment for compilation and execution.
