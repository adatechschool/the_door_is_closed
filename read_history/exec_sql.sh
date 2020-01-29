#!/usr/bin/env bash

script_sql="script_get_history.sql"

script_bsh=$(dirname $(realpath -s $0))
script_sql="/script_get_history.sql"
exec_tran="${script_bsh}${script_sql}"

sqlite3 < $exec_tran
read
