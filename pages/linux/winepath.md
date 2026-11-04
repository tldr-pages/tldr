# winepath

> Convert file paths between Windows and Unix formats for a Wine prefix.
> More information: <https://manned.org/winepath>.

- Convert a Windows path to a Unix path:

`winepath {{[-u|--unix]}} '{{C:\path\to\file}}'`

- Convert a Unix path to a long Windows path:

`winepath {{[-w|--windows]}} {{path/to/file}}`

- Convert a short (8.3) Windows path of an existing file to its long form:

`winepath {{[-l|--long]}} '{{C:\PROGRA~1}}'`

- Convert a long Windows path of an existing file to its short (8.3) form:

`winepath {{[-s|--short]}} '{{C:\Program Files}}'`

- Separate output paths with a null character instead of a newline:

`winepath {{[-u|--unix]}} -0 {{path1 path2 ...}}`

- Display help:

`winepath {{[-h|--help]}}`
