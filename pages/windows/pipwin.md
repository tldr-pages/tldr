# pipwin

> Complementary tool to install unofficial Python package binaries on Windows.
> More information: <https://github.com/lepisma/pipwin>.

- List all available packages for download:

`pipwin list`

- Search packages:

`pipwin search {{partial_name/name}}`

- Install a package:

`pipwin install {{package_name}}`

- Uninstall a package (can directly use pip for this):

`pipwin uninstall {{package_name}}`

- Download only (to a specific directory if provided):

`pipwin download --dest={{path/to/directory}} {{package_name}}`

- Install from requirements file:

`pipwin install --file={{path/to/requirements.txt}}`
