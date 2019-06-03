# vsce

> Extension manager for Visual Studio Code.
> More information: <https://github.com/microsoft/vscode-vsce>.

- List all the extensions created by a publisher:

`vsce list {{publisher}}`

- Publish an extension as major, minor or patch version:

`vsce publish {{major|minor|patch}}`

- Unpublish an extension:

`vsce unpublish {{extension_id}}`

- Package the current working directory as .vsix file:

`vsce package`

- Show the metadata associated with an extension:

`vsce show {{extension_id}}`
