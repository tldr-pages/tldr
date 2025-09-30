# mimikatz crypto

> Manipulate Windows cryptographic services and certificates.
> More information: <https://github.com/gentilkiwi/mimikatz>.

- List cryptographic providers:

`mimikatz "crypto::providers"`

- List keys in a cryptographic provider:

`mimikatz "crypto::capi"`

- Export certificates and keys:

`mimikatz "crypto::certificates /export"`
