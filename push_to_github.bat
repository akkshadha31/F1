@echo off
title Push F1 Race Intelligence to GitHub (akkshadha31)
color 0C
echo ==============================================================================
echo   🏎️  FORMULA 1 RACE INTELLIGENCE DASHBOARD - GITHUB PUSH UTILITY
echo   Author: Akkshadha Rathore
echo   Target: https://github.com/akkshadha31/F1
echo ==============================================================================
echo.

cd /d "%~dp0"

echo [1/3] Verifying Git Status & Branch...
git status -s

echo.
echo [2/3] Verifying Remote Destination...
git remote -v

echo.
echo [3/3] Pushing to https://github.com/akkshadha31/F1 (Branch: main)...
echo (A GitHub login browser window may pop up - please authorize 'akkshadha31')
echo.

git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==============================================================================
    echo   ✅ SUCCESS! All code, templates, assets, and documentation are now live at:
    echo      https://github.com/akkshadha31/F1
    echo ==============================================================================
) else (
    echo.
    echo ==============================================================================
    echo   ⚠️ PUSH NOTICE:
    echo   If you were prompted to sign in, please complete the sign-in with your
    echo   GitHub account (akkshadha31).
    echo ==============================================================================
)

echo.
pause
