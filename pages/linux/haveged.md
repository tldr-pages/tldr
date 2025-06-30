# haveged

> Hardware-based random number generator.
> More information: <https://manned.org/haveged>.

- Generate a random number:

`sudo haveged`

- Run `haveged` in foreground:

`sudo haveged {{[-F|--Foreground]}}`

- Set file path for output of `haveged`:

`sudo haveged {{[-f|--file]}} {{path/to/file}}`

- Set run level for daemon:

`sudo haveged {{[-r|--run]}} {{runlevel}}`

- Set collection buffer size in kibibyte words:

`sudo haveged {{[-b|--buffer]}} {{buffersizeinKW}}`

- Insert a command to an already running `haveged` process or daemon:

`sudo haveged {{[-c|--command]}} {{command}}`

- Set cache size in kibibyte words:

`sudo haveged {{[-d|--data]}} {{cachesizeinKW}}`

- Set number of bytes to write to the output file:

`sudo haveged {{[-n|--number]}} {{byteamount}}`
