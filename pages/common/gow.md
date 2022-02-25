# gow

> Watches Go files and restarts the app on changes.
> More information: <https://github.com/mitranim/gow>.

- Start and watch the current directory:

`gow run .`

- Pass arguments to the app

`gow run . {{argument1 argument2 ...}}`

- Watch subdirectories in verbose mode

`gow -v -w={{dir1,dir2 ...}} run .`

- Watch the specified file extensions:

`gow -e={{go,html ...}} run .`

- Help

`gow -h`
