# mimikatz process

> Manage process privileges and tokens.
> More information: <https://github.com/gentilkiwi/mimikatz>.

- List processes with their tokens:

`mimikatz "process::list"`

- Elevate mimikatz to a SYSTEM process:

`mimikatz "process::token /user:NT AUTHORITY\SYSTEM"`
