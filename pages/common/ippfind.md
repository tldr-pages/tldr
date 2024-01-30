# ippfind

> Find services registered with a DNS server or available through local devices.
> See also: `ipptool`, `ippeveprinter`.
> More information: <https://openprinting.github.io/cups/doc/man-ippfind.html>.

- List IPP printers registered on the network with their status:

`ippfind --ls`

- Send a PostScript test page for every PostScript printer on the network:

`ippfind --txt-pdl application/postscript --exec ipptool -f onepage-letter.ps '{}' print-job.test \;`

- Send a PostScript test page for every PostScript printer on the network which name matches a regex:

`ippfind --txt-pdl application/postscript --host {{regex}} --exec ipptool -f onepage-letter.ps '{}' print-job.test \;`
