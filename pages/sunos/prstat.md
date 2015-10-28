# prstat

> Report active process statistics

- examine all processes and reports statistics sorted by CPU usage

`prstat`

- examine all processes and reports statistics sorted by memory usage

`prstat -s rss`

- report total usage summary for each user

`prstat -t`

- report microstate process accounting information

`prstat -m`

- Print out a list of top 5 cpu using processes every second.

`prstat -c -n 5 -s cpu 1`
