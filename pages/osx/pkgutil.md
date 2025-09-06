# pkgutil

> Query and manipulate Mac OS X Installer packages and receipts.
> More information: <https://keith.github.io/xcode-man-pages/pkgutil.1.html>.

- List package IDs for all installed packages:

`pkgutil --pkgs`

- Verify cryptographic signatures of a package file:

`pkgutil --check-signature {{path/to/filename.pkg}}`

- List all the files for an installed package given its ID:

`pkgutil --files {{com.microsoft.Word}}`

- Extract the contents of a package file into a directory:

`pkgutil --expand-full {{path/to/filename.pkg}} {{path/to/directory}}`
