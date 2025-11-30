# travis

> Interface with Travis CI.
> More information: <https://github.com/travis-ci/travis.rb#command-line-client>.

- Authenticate the CLI client against the server, using an authentication token:

`travis login`

- List repositories the user has permissions on:

`travis repos`

- Encrypt values in `.travis.yml`:

`travis encrypt {{token}}`

- Generate a `.travis.yml` file and enable the project:

`travis init`

- Display version:

`travis version`
