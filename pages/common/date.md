# date

> Set or display the system date.
> More information: <https://www.gnu.org/software/coreutils/date>.

- Display the current date using the default locale's format:

`date +"%c"`

- Display the current date in UTC and ISO 8601 format:

`date -u +"%Y-%m-%dT%H:%M:%S%Z"`

- Display the current date as a Unix timestamp (seconds since the Unix epoch):

`date +%s`

- Display a specific date (represented as a Unix timestamp) using the default format:

`date -d @1473305798`

- Convert a specific date to the Unix timestamp format:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- Display the current date using the RFC-3339 format (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339=s`
