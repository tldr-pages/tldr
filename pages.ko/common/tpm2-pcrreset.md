# tpm2 pcrreset

> 하나 이상의 PCR 뱅크를 초기화.
> 참고: 운영체제의 locality에서는, PCR 16과 23만 초기화할 수 있음.
> 더 많은 정보: <https://manned.org/tpm2_pcrreset>.

- PCR 23 뱅크 초기화:

`tpm2 pcrreset 23`

- PCR 16과 23 뱅크 초기화:

`tpm2 pcrreset 16 23`
