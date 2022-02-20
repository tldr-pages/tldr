# Go Watch

> Watches Go files and restarts the app on changes.
> More information: <https://github.com/mitranim/gow>.

- Start and watch current directory:

`gow run .`

- Pass arguments to the app

`gow run . {{arg1 arg2 ...}}`

- Watch subdirectories in verbose mode

`gow -v -w={{dir1,dir2 ...}} run .`

- Specify file extensions to watch

`gow -e={{go,html ...}} run .`

- Help

`gow -h`
