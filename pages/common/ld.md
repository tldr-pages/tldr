# ld

> The GNU ELF linker.
> More information: <https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_mono/ld.html>.

- Link an object file with no dependencies into an executable:

`ld {{path/to/file.o}} --output {{path/to/output_executable}}`

- Link two object files together:

`ld {{path/to/file1.o}} {{path/to/file2.o}} --output {{path/to/output_executable}}`

- Dynamically link a 64-bit program to glibc (file paths change depending on system):

`ld --output {{executable}} -dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{file.o}} /lib/crtn.o`
