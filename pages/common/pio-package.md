# pio package

> Manage packages in the registry.
> Packages can only be removed within 72 hours from the published date.
> More information: <https://docs.platformio.org/en/latest/core/userguide/package/index.html>.

- Create a tarball from the current package directory:

`pio package pack --output {{path/to/output_tarball}}`

- Publish the current package directory:

`pio package publish`

- Publish the current package directory and restrict public access to it:

`pio package publish --private`

- Publish a specific package:

`pio package publish {{path/to/package}}`

- Publish a specific package and set custom release date and time (UTC):

`pio package publish {{path/to/package}} --released-at "{{2021-04-08 21:15:38}}"`

- Remove all versions of a published package from the registry:

`pio package unpublish {{package_name}}`

- Remove a specific version of a published package from the registry:

`pio package unpublish {{package_name}}@{{version}}`

- Undo the removal, putting all or a specific version of the package back into the registry:

`pio package unpublish --undo {{package_name}}@{{version}}`
