# fscrypt

> Go eszköz a Linux fájlrendszerek titkosításának kezelésére. További információ: <https://github.com/google/fscrypt>.

- Készítse elő a gyökér fájlrendszert az fscrypt használatára:

`fscrypt setup`

- Engedélyezze a fájlrendszer titkosítását egy könyvtár számára:

`fscrypt encrypt {{path/to/directory}}`

- Titkosított könyvtár feloldása:

`fscrypt unlock {{path/to/encrypted_directory}}`

- Titkosított könyvtár zárolása:

`fscrypt lock {{path/to/encrypted_directory}}`
