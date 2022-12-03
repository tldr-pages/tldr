# plutil

> View, convert, validate, or edit property list ("plist") files.
> More information: <https://www.manpagez.com/man/1/plutil/>.

- Display the contents of one or more plist files in human-readable format:

`plutil -p {{file1.plist file2.plist ...}}`

- Convert one or more plist files to XML format, overwriting the original files in-place:

`plutil -convert xml1 {{file1.plist file2.plist ...}}`

- Convert one or more plist files to binary format, overwriting the original files in-place:

`plutil -convert binary1 {{file1.plist file2.plist ...}}`

- Convert a plist file to a different format, writing to a new file:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{path/to/file.plist}} -o {{path/to/new_file.plist}}`

- Convert a plist file to a different format, writing to `stdout`:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{path/to/file.plist}} -o -`
