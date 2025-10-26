# npm rebuild

> Rebuild native Node.js packages after Node or dependency changes.
> More information: <https://docs.npmjs.com/cli/npm-rebuild>.

- Rebuild a specific package:

`npm {{[rb|rebuild]}} {{package}}`

- Rebuild all installed packages:

`npm {{[rb|rebuild]}}`

- Rebuild with verbose output:

`npm {{[rb|rebuild]}} --verbose`

- Rebuild a package in a specific directory:

`npm {{[rb|rebuild]}} --prefix {{path/to/dir}} {{package}}`

- Rebuild without using the npm cache:

`npm {{[rb|rebuild]}} --no-cache`

- Rebuild in global mode:

`npm {{[rb|rebuild]}} {{[-g|--global]}}`
