# pio pkg

> Manage packages in the registry.
> Packages can only be removed within 72 hours (3 days) from the date that they are published.
> More information: <https://docs.platformio.org/en/latest/core/userguide/package/>.

- Create a package tarball from the current directory:

`pio pkg pack {{[-o|--output]}} {{path/to/package.tar.gz}}`

- Create and publish a package tarball from the current directory:

`pio pkg publish`

- Publish the current directory and restrict public access to it:

`pio pkg publish --private`

- Publish a package:

`pio pkg publish {{path/to/package.tar.gz}}`

- Publish a package with a custom release date (UTC):

`pio pkg publish {{path/to/package.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- Remove all versions of a published package from the registry:

`pio pkg unpublish {{package}}`

- Remove a specific version of a published package from the registry:

`pio pkg unpublish {{package}}@{{version}}`

- Undo the removal, putting all versions or a specific version of the package back into the registry:

`pio pkg unpublish --undo {{package}}@{{version}}`
