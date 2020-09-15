# plutil

> View, convert, validate, or edit property list ("plist") files.

- Dump the contents of plist files in human-readable format:

`plutil -p {{file1.plist}} {{file2.plist}}`

- Convert plist files to XML format, overwriting the original files in-place:

`plutil -convert xml1 {{file1.plist}} {{file2.plist}}`

- Convert plist files to binary format, overwriting the original files in-place:

`plutil -convert binary1 {{file1.plist}} {{file2.plist}}`

- Convert a single plist file to a different format, writing to a new file:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{file.plist}} -o {{new_file.plist}}`

- Convert a single plist file to a different format, writing to stdout:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{file.plist}} -o -`

