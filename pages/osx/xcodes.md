# xcodes

> Download, install and manage multiple Xcode versions.
> See also: `xcodes runtimes`.
> More information: <https://github.com/xcodesorg/xcodes>.

- List all installed Xcode versions:

`xcodes installed`

- List all available Xcode versions:

`xcodes list`

- Select an Xcode version by specifying a version number or a path:

`xcodes select {{xcode-version|path/to/Xcode.app}}`

- Download and install a specific Xcode version:

`xcodes install {{xcode-version}}`

- Install the latest Xcode release and select it:

`xcodes install --latest --select`

- Download a specific Xcode version archive to a given directory without installing it:

`xcodes download {{xcode-version}} --directory {{path/to/directory}}`
