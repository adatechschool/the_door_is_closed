#!/usr/bin/env bash

chrome_hist="C:\Documents and Settings\Nydragon\Local Settings\Application Data\Google\Chrome\User Data\Default\History"
script_sql="script_get_history.sql"
script_sql="C:\Users\Nydragon\Documents\GitHub\the_door_is_closed\read_history\script_get_history.sql"

echo $chrome_hist
echo $script_sql

sqlite3 $chrome_hist < $script_sql
# sqlite3 "..\script_get_history.sql"

read
