<img width="2560" height="1361" alt="image" src="https://github.com/user-attachments/assets/10d79ca0-ba51-4b9e-a9bc-4e184a3ec52a" /># sfdk emulator

> Maintains and controls emulators.
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
