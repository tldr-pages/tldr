# ippeveprinter

> A simple IPP Everywhere printer server.
> See also: `ippeveps`, `ippevepcl`.
> More information: <https://openprinting.github.io/cups/doc/man-ippeveprinter.html>.

- Run the server with a specific service name:

`ippeveprinter "{{service_name}}"`

- Load printer attributes from a PPD file:

`ippeveprinter -P {{path/to/file.ppd}} "{{service_name}}"`

- Run the `file` command whenever a job is sent to the server:

`ippeveprinter -c {{/usr/bin/file}} "{{service_name}}"`

- Specify the directory that will hold the print files (by default, a directory under the user's temporary directory):

`ippeveprinter -d {{spool_directory}} "{{service_name}}"`

- Keep the print documents in the spool directory rather than deleting them:

`ippeveprinter -k "{{service_name}}"`

- Specify the printer speed in pages/minute unit (10 by default):

`ippeveprinter -s {{speed}} "{{service_name}}"`
