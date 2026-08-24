# spindump

> Profile entire system during a time interval.
> Used for normal application force quits to display a dialog offering details and the option to report to Apple.
> More information: <https://keith.github.io/xcode-man-pages/spindump.8.html>.

- Sample all processes for 10 seconds with 10 milliseconds of run time between samples:

`sudo spindump`

- Sort a specific process topmost for a custom duration and interval:

`sudo spindump {{pid|partial_name}} {{duration_seconds}} {{interval_milliseconds}}`

- Write output to a specific file:

`sudo spindump {{pid|partial_name}} -o {{path/to/output.txt}}`
