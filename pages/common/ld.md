# ld

> The GNU ELF linker.
> More information: <https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_mono/ld.html>.

- "Link" an object file with no dependencies into an executable:

`ld {{file.o}} -o {{executable}}`

- Link two object files together:

`ld {{file.o}} {{file1.o}} -o {{executable}}`

- Dynamically link a 64-bit program to glibc (file paths change depending on system):

`ld -o {{executable}} -dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{file.o}} /lib/crtn.o`
