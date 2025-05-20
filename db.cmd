@echo off
:: مسیر نسبی به پوشه PostgreSQL Portable
set PG_PATH=.\.env\pgsql\bin
set PG_DATA=.\.env\pgsql\data

:: راه‌اندازی PostgreSQL
echo Starting PostgreSQL...
%PG_PATH%\pg_ctl -D %PG_DATA% start