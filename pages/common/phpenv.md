# phpenv

> A PHP version manager for development purposes.
> More information: <https://github.com/phpenv/phpenv>.

- Install a PHP version globally:

`phpenv install {{version}}`

- Refresh shim files for all PHP binaries known to `phpenv`:

`phpenv rehash`

- List all installed PHP versions:

`phpenv versions`

- Display the currently active PHP version:

`phpenv version`

- Set the global PHP version:

`phpenv global {{version}}`

- Set the local PHP version, which overrides the global version:

`phpenv local {{version}}`

- Unset the local PHP version:

`phpenv local --unset`
