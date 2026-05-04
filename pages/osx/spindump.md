# spindump

> Profile entire system during a time interval.
> Used for normal application force quits to display a dialog offering details and the option to report to Apple.
> More information: <https://keith.github.io/xcode-man-pages/spindump.8.html>.

- Sample all processes for 10 seconds with 10 milliseconds of run time between samples:

`sudo spindump`

- Prioritize specified process in output with optional sampling duration and sample interval:

`sudo spindump {{pid|partial-name}} {{sampling-duration-seconds}} {{sampling-interval-milliseconds}}`

- Write output to a specific file:

`sudo spindump {{pid|partial-name}} -o {{path/to/output.txt}}`
