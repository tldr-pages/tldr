# byzanz-record

> Record the screen.
> More information: <https://manned.org/byzanz-record>.

- Record the screen and write the recording to a file (by default, `byzanz-record` will only record for 10 seconds):

`byzanz-record {{path/to/file.ext}}`

- Show information while and after recording:

`byzanz-record {{[-v|--verbose]}} {{path/to/file.ext}}`

- Record the screen for a minute:

`byzanz-record {{[-d|--duration]}} 60 {{path/to/file.ext}}`

- Delay recording for 10 seconds:

`byzanz-record --delay 10 {{path/to/file.ext}}`
