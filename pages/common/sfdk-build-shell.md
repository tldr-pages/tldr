# sfdk build-shell

> Execute custom steps in build engine.
> See also: `sfdk config` for configuring the build target and `sfdk build-init` for initializing build tree.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.build-shell.adoc>.

- Launch interactive shell in the build engine:

`sfdk build-shell`

- Run a specified command in the build shell:

`sfdk build-shell {{command}}`

- Launch interactive shell in the build engine in maintenance mode, when inspecting or modifying the build environment:

`sfdk build-shell --maintain`
