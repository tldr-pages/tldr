# pio package

> Manage packages in the registry.
> Packages can only be removed within 72 hours (3 days) from the date that they are published.
> More information: <https://docs.platformio.org/en/latest/core/userguide/package/>.

- Create a package tarball from the current directory:

`pio package pack --output {{path/to/package.tar.gz}}`

- Create and publish a package tarball from the current directory:

`pio package publish`

- Publish the current directory and restrict public access to it:

`pio package publish --private`

- Publish a package:

`pio package publish {{path/to/package.tar.gz}}`

- Publish a package with a custom release date (UTC):

`pio package publish {{path/to/package.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- Remove all versions of a published package from the registry:

`pio package unpublish {{package_name}}`

- Remove a specific version of a published package from the registry:

`pio package unpublish {{package_name}}@{{version}}`

- Undo the removal, putting all versions or a specific version of the package back into the registry:

`pio package unpublish --undo {{package_name}}@{{version}}`
