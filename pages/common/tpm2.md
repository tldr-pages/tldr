# tpm2

> A single small executable that combines the various tpm2-tools.
> Some subcommands such as `pcrread`, `pcrreset`, etc. have their own usage documentation.
> More information: <https://manned.org/tpm2>.

- Reset the PCR 16 banks:

`tpm2 pcrreset 16`

- Extend the PCR 16 sha1 bank with `f1d2d2f924e986ac86fdf7b36c94bcdf32beec15`:

`tpm2 pcrextend 16:sha1=f1d2d2f924e986ac86fdf7b36c94bcdf32beec15`

- Read the PCR 16 sha1 bank:

`tpm2 pcrread sha1:16`

- Display help:

`tpm2 {{[-h|--help]}}`
