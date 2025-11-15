# mimikatz dpapi

> Interact with the Windows Data Protection API (DPAPI).
> More information: <https://github.com/gentilkiwi/mimikatz>.

- List master keys:

`mimikatz "dpapi::masterkey /list"`

- Decrypt a DPAPI blob:

`mimikatz "dpapi::blob /in:blob_file.bin"`

- Retrieve Chrome credentials using DPAPI:

`mimikatz "dpapi::chrome /in:Login Data"`
