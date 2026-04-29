# tpm2 pcrreset

> Reset one or more PCR banks.
> Note: On operating system's locality, only PCR 16 and 23 can be reset.
> More information: <https://manned.org/tpm2_pcrreset>.

- Reset the PCR 23 banks:

`tpm2 pcrreset 23`

- Reset the PCR 16 and 23 banks:

`tpm2 pcrreset 16 23`
