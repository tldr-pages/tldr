# tmt run

> Execute tmt test steps. By default, all steps are run.
> More information: <https://tmt.readthedocs.io/en/stable/overview.html#run>.

- Run all test steps for each plan:

`tmt run`

- Run only the discover step to show what tests would be run:

`tmt run discover -v`

- Run all steps and adjust the provision step options:

`tmt run --all provision --how {{container}} --image {{fedora:rawhide}}`

- Run only selected plans and tests:

`tmt run plan --name {{/plan/name}} test --name {{/test/name}}`

- Show results from the last run in a web browser:

`tmt run --last report --how {{html}} --open`

- Run tests with the provided context:

`tmt run --context {{key=value}} -c {{distro=fedora}}`

- Run tests interactively (debug test code in the middle of a test):

`tmt run --all execute --how {{tmt}} --interactive`

- Use dry mode to see what actions would happen and use the highest verbosity:

`tmt run --dry -vvv`
