# pwn

> Exploit Development Library designed for rapid prototyping.
> More information: <https://docs.pwntools.com/en/stable/commandline.html>.

- Convert  the given assembly code to `bytes`:

`pwn asm "{{xor edi, edi}}"`

- Create a cyclic pattern of the specific number of characters:

`pwn cyclic {{number}}`

- Encode the given data into the hexadecimal system:

`pwn hex {{deafbeef}}`

- Decode the given data from hexadecimal:

`pwn unhex {{6c4f7645}}`

- Print a x64 Linux shellcode for running a shell:

`pwn shellcraft {{amd64.linux.sh}}`

- Check the binary security settings for the given ELF file:

`pwn checksec {{path/to/file}}`

- Check for Pwntools updates:

`pwn update`

- Display version:

`pwn version`
