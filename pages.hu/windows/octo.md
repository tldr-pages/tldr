# octo

> Parancssori eszközök az Octopus Deploy számára. További információ: <https://octopus.com/docs/octopus-rest-api/octo.exe-command-line>.

- Csomag létrehozása:

`octo pack --id={{package_name}}`

- Csomagot helyezhet el az Octopus kiszolgálón lévő tárolóhelyre:

`octo push --package={{package_name}}`

- Kiadás létrehozása:

`octo create-release --project={{project_name}} --packageversion={{version}}`

- Kiadás telepítése:

`octo deploy-release --project={{project_name}} --packageversion={{version}} --deployto={{environment_name}} --tenant={{deployment_target}}`
