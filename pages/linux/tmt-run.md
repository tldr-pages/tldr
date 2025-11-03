# tmt run

> Execute tmt test steps. By default, all steps are run.
> More information: <https://tmt.readthedocs.io/en/stable/stories/cli.html#run>.

- Run all test steps for each plan:

`tmt run`

- Run only the discover step to show what tests would be run:

`tmt run discover {{[-v|--verbose]}}`

- Run all steps and adjust the provision step options:

`tmt run {{[-a|--all]}} provision {{[-h|--how]}} {{container}} {{[-i|--image]}} {{fedora:rawhide}}`

- Run only selected plans and tests:

`tmt run plan {{[-n|--name]}} {{/plan/name}} test {{[-n|--name]}} {{/test/name}}`

- Show results from the last run in a web browser:

`tmt run {{[-l|--last]}} report {{[-h|--how]}} {{html}} {{[-o|--open]}}`

- Run tests with the provided context:

`tmt run {{[-c|--context]}} {{key=value}} {{[-c|--context]}} {{distro=fedora}}`

- Run tests interactively (debug test code in the middle of a test):

`tmt run {{[-a|--all]}} execute {{[-h|--how]}} {{tmt}} --interactive`

- Use dry mode to see what actions would happen and use the highest verbosity:

`tmt run {{[-n|--dry]}} {{[-vvv|--verbose --verbose --verbose]}}`
