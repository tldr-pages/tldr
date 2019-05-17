# fselect

> Find files with SQL-like queries.
> Homepage: <https://github.com/jhspetersson/fselect>.

- Select full path and size from temporary or config files in a given directory:

`fselect size, path from {{path/to/directory}} where name = {{'*.cfg'}} or name = {{'*.tmp'}}`

- Find square images:

`fselect path from {{path/to/directory}} where width = height`

- Find old-school rap 320kbps MP3 files:

`fselect path from /home/user/music where genre = Rap and bitrate = 320 and mp3_year lt 2000`

- Output as json:

`fselect size, path from /home/user limit 5 into json`

- Aggregate functions:

`fselect "MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*) from /home/user/Downloads"`
