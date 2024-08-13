# date

> Set or display the system date.
> More information: <https://keith.github.io/xcode-man-pages/date.1.html>.

- Display the current date using the default locale's format:

`date +%c`

- Display the current date in UTC and ISO 8601 format:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Display the current date as a Unix timestamp (seconds since the Unix epoch):

`date +%s`

- Display a specific date (represented as a Unix timestamp) using the default format:

`date -r {{1473305798}}`
