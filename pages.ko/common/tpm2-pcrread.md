# tpm2 pcrread

> TPM에서 PCR 값을 읽음.
> 더 많은 정보: <https://manned.org/tpm2_pcrread>.

- 모든 PCR 값 읽기:

`tpm2 pcrread`

- sha256 뱅크의 모든 PCR 값 읽기:

`tpm2 pcrread sha256:all`

- 여러 뱅크에서 지정한 PCR 값을 읽어 파일에 저장:

`tpm2 pcrread {{[-o|--output]}} {{경로/대상/파일}} {{sha1:16,17,18+sha256:16,17,18}}`
