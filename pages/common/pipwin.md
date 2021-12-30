# pip

> complementary tool for pip on Windows.
> pipwin installs unofficial python package binaries for windows provided by Christoph Gohlke <http://www.lfd.uci.edu/~gohlke/pythonlibs/>
> More information: <https://github.com/lepisma/pipwin>.
- List all available packages for download:

`pipwin list`

- Search packages:

`pipwin search {{partial_name/name}}`

- Install a package:

`pipwin install {{package_name}}`

- Uninstall a package(Can directly use pip for this):

`pipwin uninstall {{package_name}}`

- Download only (to special directory if provided):

`pipwin download -d {{path/to/directory}} {{package_name}}`

- install from requirements file:

`pipwin install -r {{path/to/requirements.txt}}`