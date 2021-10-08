# checkinstall

> Track the local installation of a software package, and produce a binary package which can be managed via your native package manager.
> More information: <http://checkinstall.izto.org/>.

- Create and install the package with default settings:

`sudo checkinstall -y`

- Create the package but do not install:

`sudo checkinstall --install=no`

- Create the package without docs:

`sudo checkinstall --nodoc`

- Create the package and set the name:

`sudo checkinstall --pkgname {{package}}`

- Create the package and specify where to save it:

`sudo checkinstall --pakdir {{path/to/<placeholder>}}`
