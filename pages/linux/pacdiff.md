# pacdiff

> Maintenance utility for `.pacorig`, `.pacnew` and `.pacsave` files created by `pacman`.
> More information: <https://manned.org/pacdiff>.

- Review files that need maintenance in interactive mode:

`pacdiff`

- Use sudo and sudoedit to remove and merge files:

`pacdiff {{[-s|--sudo]}}`

- Review files needing maintenance, creating `.bak`ups of the original if you `(O)verwrite`:

`pacdiff {{[-s|--sudo]}} {{[-b|--backup]}}`

- Use a specific editor to view and merge configuration files (default is `vim -d`):

`DIFFPROG={{editor}} pacdiff`

- Scan for configuration files with `locate` instead of using `pacman` database:

`pacdiff {{[-l|--locate]}}`

- Display help:

`pacdiff {{[-h|--help]}}`
