# sfdk emulator

> Maintain and control emulators.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/40-testing-maintain/doc/command.emulator.adoc>.

- Display the installed emulators:

`sfdk emulator list`

- Start an emulator:

`sfdk emulator start {{name}}`

- Stop an emulator:

`sfdk emulator stop {{name}}`

- Display emulator status:

`sfdk emulator status {{name}}`

- Run an interactive shell on an emulator:

`sfdk emulator exec {{emulator}}`

- Execute a command on an emulator:

`sfdk emulator exec {{emulator}} {{command}}`

- Set a property:

`sfdk emulator set {{name}} {{property}}={{value}}`

- Show emulator properties:

`sfdk emulator show {{name}}`
