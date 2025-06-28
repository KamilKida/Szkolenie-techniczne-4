@echo off
REM Przechodzimy do katalogu projektu
cd /d %~dp0

REM Aktywujemy virtualenv (dla Windows)
call venv\Scripts\activate.bat

REM Uruchamiamy aplikację python
python main.py

REM Czekamy na wciśnięcie klawisza, żeby okno się nie zamknęło
pause
