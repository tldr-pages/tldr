# ipptool

> Issue IPP requests and receive printer's/server's responses.
> See also: `ippfind`, `ippeveprinter`.
> More information: <https://openprinting.github.io/cups/doc/man-ipptool.html>.

- Get all attributes and their values supported by a printer:

`ipptool ipp://{{printer_uri}} get-completed-jobs.test`

- Get the list of completed jobs of a printer:

`ipptool ipp://{{printer_uri}} get-completed-jobs.test`

- Send an email notification when a printer changes:

`ipptool -d recipient=mailto:{{email}} ipp://{{printer_uri}} create-printer-subscription.test`
