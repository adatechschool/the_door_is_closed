.cd "C:/Documents and Settings/Nydragon/Local Settings/Application Data/Google/Chrome/User Data/Default"
.open History
.mode csv
.cd "C:/Users/Nydragon/Documents/GitHub/the_door_is_closed/read_history"
.output data.csv
SELECT id, url
FROM urls;
