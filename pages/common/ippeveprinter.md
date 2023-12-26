# ippeveprinter

> A simple IPP Everywhere printer server.
> See also: `ippeveps`, `ippevepcl`.
> More information: <https://www.cups.org/doc/man-ippeveprinter.html>.

- Run the server with a service name of "My Fake Printer":

`ippeveprinter {{"My fake Printer"}}`

- Load printer attributes from a PPD file:

`ippeveprinter -P {{path/to/file.ppd}} {{"My Fake Printer"}}`

- Run the `file` command whenever a job is sent to the server:

`ippeveprinter -c {{/usr/bin/file}} {{"My fake Printer"}}`

- Specify the directory that will hold the print files (by default, a directory under the user's temporary directory):

`ippeveprinter -d {{spool_directory}} {{"My Fake Printer"}}`

- Keep the print documents in the spool directory rather than deleting them:

`ippeveprinter -k {{"My fake Printer"}}`

- Specify the printer speed in pages/min (10 by default):

`ippeveprinter -s {{speed}} {{"My Fake Printer"}}`
