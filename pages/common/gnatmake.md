# gnatmake

> A low-level build tool for Ada programs (part of the GNAT toolchain).
> More information: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Building-with-gnatmake.html>.

- Compile an executable:

`gnatmake {{source_file1.adb source_file2.adb ...}}`

- Set a custom executable name:

`gnatmake -o {{path/to/executable}} {{path/to/file.adb}}`

- [f]orce recompilation:

`gnatmake -f {{path/to/file.adb}}`
