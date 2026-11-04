# tpm2 pcrextend

> PCR 값을 확장.
> 더 많은 정보: <https://manned.org/tpm2_pcrextend>.

- sha1 뱅크의 PCR 16 값을 확장:

`tpm2 pcrextend 16:sha1={{f1d2d2f924e986ac86fdf7b36c94bcdf32beec15}}`

- sha1 및 sha256 뱅크의 PCR 16 값을 각각 확장:

`tpm2 pcrextend 16:sha1={{f1d2d2f924e986ac86fdf7b36c94bcdf32beec15}},sha256={{b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c}}`

- sha1 뱅크의 PCR 16과 sha256 뱅크의 PCR 23 값을 확장:

`tpm2 pcrextend 16:sha1={{f1d2d2f924e986ac86fdf7b36c94bcdf32beec15}} 23:sha256={{b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c}}`
