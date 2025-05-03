# sfdk check

> Performs quality checks.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.cmake.adoc>.

- Display test suites:

`sfdk check --list-suites`

- Run all or essential test suites:

`sfdk check`

- Add testing level to the check:

`sfdk check {{[-l|--levels]}} +{{level}}`

- Remove testing level from the check:

`sfdk check {{[-l|--levels]}} -{{level}}`

- Add testing suite to the check:

`sfdk check {{[-s|--suites]}} +{{suite}}`

- Remove testing suite from the check:

`sfdk check {{[-s|--suites]}} -{{suite}}`
