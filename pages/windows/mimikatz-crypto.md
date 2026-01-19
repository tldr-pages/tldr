# mimikatz crypto

> Manipulates Windows cryptographic services and certificates, allowing you to list and export certificates and keys, even those marked as non-exportable. > It generally requires elevated privileges, especially when accessing system keys.
> More information: <https://github.com/gentilkiwi/mimikatz>.

- List cryptographic providers:

`mimikatz "crypto::providers"`

- List keys in a cryptographic provider:

`mimikatz "crypto::capi"`

- Export certificates and keys:

`mimikatz "crypto::certificates /export"`
