# winepath

> Convert file paths between Windows and Unix formats for a Wine prefix.
> More information: <https://manned.org/winepath>.

- Convert a Windows path to a [u]nix path:

`winepath -u '{{C:\path\to\file}}'`

- Convert a Unix path to a long [w]indows path:

`winepath -w {{path/to/file}}`

- Convert a short (8.3) Windows path of an existing file to its [l]ong form:

`winepath -l '{{C:\PROGRA~1}}'`

- Convert a long Windows path of an existing file to its [s]hort (8.3) form:

`winepath -s '{{C:\Program Files}}'`

- Separate output paths with a null character instead of a newline:

`winepath -u -0 {{path1 path2 ...}}`

- Display help:

`winepath --help`
