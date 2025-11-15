# olevba

> Parse OLE and OpenXML files (e.g., DOC, XLS, PPT, etc.) to extract VBA macros, deobfuscate, and analyze malicious code.
> Part of the `python-oletools` suite.
> More information: <https://github.com/decalage2/oletools>.

- Analyze a file, showing both macro code and analysis results:

`olevba {{path/to/file}}`

- Recursively analyze all supported files in a directory:

`olevba -r {{path/to/directory}}`

- Provide a password for encrypted Microsoft Office files (may be repeated):

`olevba {{[-p|--password]}} {{password}} {{path/to/encrypted_file}}`

- Display only analysis results, without showing macro source code:

`olevba {{[-a|--analysis]}} {{path/to/file}}`

- Display only macro source code:

`olevba {{[-c|--code]}} {{path/to/file}}`

- Show obfuscated strings and their decoded content:

`olevba --decode {{path/to/file}}`
