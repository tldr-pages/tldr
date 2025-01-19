# olevba

> Parse OLE and OpenXML files (e.g., .doc, .xls, .ppt, etc.) to extract VBA macros, deobfuscate, and analyze malicious code.
> Part of the [python-oletools](http://www.decalage.info/python/oletools) suite.
> For more information: <http://decalage.info/python/oletools>.

- Analyze a file, showing both macro code and analysis results:

`olevba {{path/to/file}}`

- Recursively analyze all supported files in a directory:

`olevba -r {{path/to/directory}}`

- Provide a password for encrypted Office files (may be repeated):

`olevba --password {{password}} {{path/to/encrypted_file}}`

- Display only analysis results, without showing macro source code:

`olevba -a {{path/to/file}}`

- Display only macro source code:

`olevba -c {{path/to/file}}`

- Show obfuscated strings and their decoded content:

`olevba --decode {{path/to/file}}`
