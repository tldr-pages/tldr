# vsce

> Bővítménykezelő a Visual Studio Code-hoz. További információ: <https://github.com/microsoft/vscode-vsce>.

- A kiadó által létrehozott összes kiterjesztés listázása:

`vsce list {{publisher}}`

- Egy bővítmény közzététele fő-, mellék- vagy javított verzióban:

`vsce publish {{major|minor|patch}}`

- Kiterjesztés visszavonása:

`vsce unpublish {{extension_id}}`

- Csomagolja az aktuális munkakönyvtárat `.vsix` fájlként:

`vsce package`

- A kiterjesztéshez tartozó metaadatok megjelenítése:

`vsce show {{extension_id}}`
