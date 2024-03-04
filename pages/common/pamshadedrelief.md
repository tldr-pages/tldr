# pamshadedrelief

> Generate a shaded relief from an elevation map.
> See also: `pamcrater`, `ppmrelief`.
> More information: <https://netpbm.sourceforge.net/doc/pamshadedrelief.html>.

- Generate a shaded relief image with the input image interpreted as an elevation map:

`pamshadedrelief < {{path/to/input.pam}} > {{path/to/output.pam}}`

- Gamma adjust the image by the specified factor:

`pamshadedrelief -gamma {{factor}} < {{path/to/input.pam}} > {{path/to/output.pam}}`
