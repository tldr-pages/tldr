# rlog

> Print the revision log of RCS files.
> See also: `ci`, `co`, `rcs`, `rcsdiff`.
> More information: <https://manned.org/rlog>.

- Display the complete revision history of a file:

`rlog {{path/to/file}}`

- Display only the header information (no revision details):

`rlog -h {{path/to/file}}`

- Display information for a specific revision:

`rlog -r{{revision}} {{path/to/file}}`

- Display revisions within a date range:

`rlog -d"{{start_date}}<{{end_date}}" {{path/to/file}}`

- Display revisions by a specific author:

`rlog -w{{author}} {{path/to/file}}`
