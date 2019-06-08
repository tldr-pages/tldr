# enca

> Detect and convert encoding of text files.
> More information: <https://github.com/nijel/enca>.

- Detect file(s) encoding according to your system's locale:

`enca {{file(s)}}`

- Detect file(s) encoding; -L option tells enca the current language; language is in the POSIX/C locale format, e.g. zh_CN, en_US etc:

`enca -L {{language}} {{file(s)}}`

- Convert file(s) to specified encoding:

`enca -L {{language}} -x {{to_encoding}} {{file(s)}}`

- Save original_file as new_file and convert new_file to specified encoding:

`enca -L {{language}} -x {{to_encoding}} < {{original_file}} > {{new_file}}`
