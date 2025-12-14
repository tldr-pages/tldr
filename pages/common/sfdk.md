# sfdk

> Frontend of the Sailfish SDK.
> Some subcommands such as `init`, `build-init`, `device` have their own usage documentation.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/10-general/doc/module.adoc>.

- Setup the current environment for building for SailfishOS 5.0.0.62 aarch64 target:

`sfdk config target=SailfishOS-5.0.0.62-aarch64`

- Initialize the current directory as the build directory:

`sfdk build-init`

- Execute build steps of the RPM SPEC file for a specific project:

`sfdk -C {{path/to/project}} build`

- List repositories in the SailfishOS 5.0.0.62 armv7hl build target:

`sfdk -c 'target=SailfishOS-5.0.0.62-armv7hl' build-shell --maintain ssu lr`

- Deploy the package to the emulator:

`sfdk config device="Sailfish OS Emulator 5.0.0.62"; sfdk deploy --sdk`

- Display help:

`sfdk --help`

- Display help for specific topic (`building`, `testing`, `maintaining`, `ide`, `all`):

`sfdk --help-{{topic}}`

- Display version:

`sfdk --version`
