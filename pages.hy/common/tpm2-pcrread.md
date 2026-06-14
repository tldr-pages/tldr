# tpm2 pcrread

> Կարդացեք PCR արժեքները TPM-ից:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/tpm2_pcrread>:.

- Կարդացեք բոլոր PCR արժեքները.:

`tpm2 pcrread`

- Կարդացեք sha256 բանկի բոլոր PCR արժեքները.:

`tpm2 pcrread sha256:all`

- Կարդացեք որոշակի PCR արժեքներ բազմաթիվ բանկերից և գրեք դրանք ֆայլում.:

`tpm2 pcrread {{[-o|--output]}} {{path/to/file}} {{sha1:16,17,18+sha256:16,17,18}}`
