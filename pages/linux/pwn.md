# pwn

> Exploit Development Library designed for rapid prototyping.
> More information: <https://docs.pwntools.com/en/stable/commandline.html>.

- Convert given assembly code to `bytes`:

`pwn asm {{'xor edi, edi'}}`

- Create a cyclic pattern of `100` characters:

`pwn cyclic {{100}}`

- Print `bytes` for the given `hex-encoded` data:

`pwn hex {{deafbeef}}`

- Print `hex-encoded` data for the given `bytes`:

`pwn unhex {{6c4f7645}}`

- Print `x64 Linux Shellcode` in bytes that runs a `shell`:

`pwn shellcraft {{amd64.linux.sh}}`

- Check binary security settings for the given `ELF file`:

`pwn checksec {{program}}`

- Check for pwntools updates:

`pwn update`

- Print Pwntools help menu:

`pwn version`
