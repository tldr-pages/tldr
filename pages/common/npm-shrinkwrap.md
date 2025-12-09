# npm shrinkwrap

> Lock down the dependencies of a package, creating a `npm-shrinkwrap.json` file.
> Similar to `package-lock.json` but intended for published packages.
> More information: <https://docs.npmjs.com/cli/shrinkwrap>.

- Generate a `npm-shrinkwrap.json` file from the current `package-lock.json`:

`npm shrinkwrap`

- Run in production mode (excludes devDependencies):

`npm shrinkwrap --production`

- Force recreate the shrinkwrap file even if it already exists:

`npm shrinkwrap --force`
