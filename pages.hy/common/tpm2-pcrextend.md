# tpm2 pcrexten

> Ընդլայնում է PCR:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/tpm2_pcrextend>:.

- Ընդլայնել sha1 բանկի PCR 16 արժեքը.:

`tpm2 pcrextend 16:sha1={{f1d2d2f924e986ac86fdf7b36c94bcdf32beec15}}`

- Ընդլայնել sha1 և sha256 բանկերի արժեքի PCR 16 արժեքը.:

`tpm2 pcrextend 16:sha1={{f1d2d2f924e986ac86fdf7b36c94bcdf32beec15}},sha256={{b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c}}`

- Ընդլայնել sha1 բանկի PCR 16 արժեքը և sha256 բանկի PCR 23 արժեքը.:

`tpm2 pcrextend 16:sha1={{f1d2d2f924e986ac86fdf7b36c94bcdf32beec15}} 23:sha256={{b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c}}`
