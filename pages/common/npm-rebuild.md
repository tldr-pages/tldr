# npm rebuild

> Rebuild native Node.js packages after Node or dependency changes.
> More information: <https://docs.npmjs.com/cli/v10/commands/npm-rebuild>.

- Rebuild a specific package:

`npm rebuild {{package}}`

- Rebuild all installed packages:

`npm rebuild`

- Rebuild with verbose output:

`npm rebuild --verbose`

- Rebuild a package in a specific directory:

`npm rebuild --prefix={{path/to/dir}} {{package}}`

- Rebuild without using the npm cache:

`npm rebuild --no-cache`

- Rebuild in global mode:

`npm rebuild -g`
