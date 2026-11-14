# sort-package-json

> Sort package manifest files according to standard Node.js conventions.
> More information: <https://github.com/keithamus/sort-package-json>.

- Sort the package manifest file in the current directory:

`sort-package-json`

- Sort multiple specific package manifest files across a workspace:

`sort-package-json "{{packages/*/package.json}}"`

- Check if the package manifest is already sorted without modifying it:

`sort-package-json --check`

- Sort the package manifest quietly without printing file names:

`sort-package-json --quiet`
