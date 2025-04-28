# sfdk build-requires

> Updates build time dependencies.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.build-requires.adoc>.

- Run a subcommand refreshing the cache:

`sfdk build-requires --refresh {{subcommand}}`

- Run a subcommand without refreshing the cache:

`sfdk build-requires --no-refresh {{subcommand}}`

- Install or update the build-time dependencies:

`sfdk build-requires pull`

- Install or update the build-time dependencies, omitting all extra ones:

`sfdk build-requires reset`

- Show the difference between current and clean build environments:

`sfdk build-requires diff`
