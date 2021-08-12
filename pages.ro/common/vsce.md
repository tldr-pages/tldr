# vsce

> Manager de extensie pentru Visual Studio Code.
> Mai multe informaţii: <https://github.com/microsoft/vscode-vsce>

- Listați toate extensiile create de un editor:

`vsce list {{publisher}}`

- Publicarea unei extensii ca versiune majoră, minoră sau patch:

`vsce publish {{major|minor|patch}}`

- Dezpublicarea unei extensii:

`vsce unpublish {{extension_id}}`

- Pachet directorul de lucru curent ca fișier `.vsix`:

`vsce package`

- Arată metadatele asociate cu o extensie:

`vsce show {{extension_id}}`
