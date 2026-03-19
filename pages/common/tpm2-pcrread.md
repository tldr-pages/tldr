# tpm2 pcrread

> Read the PCR values from a TPM.
> More information: <https://manned.org/tpm2_pcrread>.

- Read all PCR values:

`tpm2 pcrread`

- Read all PCR values of the sha256 bank:

`tpm2 pcrread sha256:all`

- Read the PCR 16, 17 and 18 values of the sha1 and sha256 banks, then write them in binary format in the pcrs file:

`tpm2 pcrread --output pcrs sha1:16,17,18+sha256:16,17,18`
