# ld

> Link object files together.
> More information: <https://sourceware.org/binutils/docs-2.38/ld.html>.

- Link a specific object file with no dependencies into an executable:

`ld {{path/to/file.o}} --output {{path/to/output_executable}}`

- Link two object files together:

`ld {{path/to/file1.o}} {{path/to/file2.o}} --output {{path/to/output_executable}}`

- Dynamically link an x86_64 program to glibc (file paths change depending on the system):

`ld --output {{path/to/output_executable}} --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{path/to/file.o}} /lib/crtn.o`
