# sfdk check

> Performs quality checks.
> More information: <https://docs.sailfishos.org/Develop/Apps/Tutorials/Building_packages_-_advanced_techniques/#validating-package-contents>.

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
