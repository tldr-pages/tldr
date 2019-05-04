# fselect

> Find files with SQL-like queries.

- Select full path and size from temporary or config files in a given directory.

`fselect size, path from /home/user where name = '*.cfg' or name = '*.tmp'`

- Find square images:

`fselect path from /home/user/Photos where width = height`

- Find old-school rap MP3 files:

`fselect path from /home/user/music where genre = Rap and bitrate = 320 and mp3_year lt 2000`

- Output as json:

`fselect size, path from /home/user limit 5 into json`

- Aggregate functions:

`fselect "MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*) from /home/user/Downloads"`
