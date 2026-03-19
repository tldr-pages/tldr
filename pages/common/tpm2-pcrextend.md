# tpm2 pcrextend

> Extends a PCR.
> More information: <https://manned.org/tpm2_pcrextend>.

- Extend the PCR 16 value of the sha1 bank:

`tpm2 pcrextend 16:sha1=f1d2d2f924e986ac86fdf7b36c94bcdf32beec15`

- Extend the PCR 16 value of the sha1 and sha256 banks value:

`tpm2 pcrextend 16:sha1=f1d2d2f924e986ac86fdf7b36c94bcdf32beec15,sha256=b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c`

- Extend the PCR 16 value of the sha1 bank and PCR 23 of the sha256 bank:

`tpm2 pcrextend 16:sha1=f1d2d2f924e986ac86fdf7b36c94bcdf32beec15 23:sha256=b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c`
