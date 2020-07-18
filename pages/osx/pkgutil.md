# pkgutil

> Query and manipulate Mac OS X Installer packages and receipts.

- List package IDs for all installed packages:

`pkgutil --pkgs`

- Verify cryptographic signatures of a package file:

`pkgutil --check-signature {{filename.pkg}}`

- List all the files for an installed package given its ID:

`pkgutil --files {{com.microsoft.Word}}`

- Extract the contents of a packge file into a directory:

`pkgutil  --expand-full {{filename.pkg}} {{directory}}`
