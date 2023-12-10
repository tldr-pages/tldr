# byzanz-record

> Create media files from screen recordings.
> More information: <https://linux.die.net/man/1/byzanz-record>.

- Record the screen and write the recording to a file (by default, byzanz-record will only record for 10 seconds):

`byzanz-record {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`

- Send a desktop notification after recording:

`byzanz-record {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}} && notify-send "Reminder" "Finished recording"`

- Record the screen for a minute:

`byzanz-record --duration 60 {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`

- Delay recording for 10 seconds:

`byzanz-record --delay 10 {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`
