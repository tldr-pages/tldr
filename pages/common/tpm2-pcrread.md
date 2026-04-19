# tpm2 pcrread

> Read the PCR values from a TPM.
> More information: <https://manned.org/tpm2_pcrread>.

- Read all PCR values:

`tpm2 pcrread`

- Read all PCR values of the sha256 bank:

`tpm2 pcrread sha256:all`

- Read specific PCR values from multiple banks and write them to a file:

`tpm2 pcrread {{[-o|--output]}} {{path/to/file}} {{sha1:16,17,18+sha256:16,17,18}}`
