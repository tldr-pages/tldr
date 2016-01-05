# enca

> Detect and convert encoding of text files

- detect file(s) encoding according to your system's locale

`enca {{file(s)}}`

- detect file(s) encoding; -L option tells enca the current language; language is in the POSIX/C locale format, e.g. zh_CN, en_US etc.

`enca -L {{language}} {{file(s)}}`

- convert file(s) to specified encoding

`enca -L {{language}} -x {{to_encoding}} {{file(s)}}`

- save original_file as new_file and convert new_file to specified encoding

`enca -L {{language}} -x {{to_encoding}} < {{original_file}} > {{new_file}}`
