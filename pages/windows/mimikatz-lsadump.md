# mimikatz lsadump

> Dump secrets from the Windows Local Security Authority (LSA).
> Requires SYSTEM privileges.
> More information: <https://github.com/gentilkiwi/mimikatz>.

- Dump SAM hashes:

`mimikatz "lsadump::sam"`

- Dump secrets from the SECURITY hive:

`mimikatz "lsadump::secrets"`

- Dump cached domain credentials:

`mimikatz "lsadump::cache"`
