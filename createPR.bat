@echo off
setlocal enabledelayedexpansion

set "message="
set "title="

:parse_args
if "%1"=="" goto :end_args
if "%1"=="-m" (
    set message=%2
    shift
    goto :parse_args
)

if "%1"=="-t" (
    set title=%2
    shift
    goto :parse_args
)
shift
goto :parse_args

:end_args


if "%message%"=="" (
    echo Please provide a message using '-m'.
    pause
    exit /b
)
if "%title%"=="" (
    echo Please provide a title using '-t'.
    pause
    exit /b
)

REM Here you can add your further processing or actions based on %message% and %title% variables.
echo Message: %message%
echo Title: %title%

python create_PR.py -t %title% -m %message%
exit /0