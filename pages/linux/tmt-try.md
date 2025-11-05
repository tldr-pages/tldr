# tmt try

> Quickly experiment with tests and environments.
> More information: <https://tmt.readthedocs.io/en/stable/stories/cli.html#try>.

- Quickly experiment with the default provision method (no tests in the CWD):

`tmt try`

- Run a test in the current working directory:

`cd {{path/to/test_directory}} && tmt try`

- Use a specific operating system:

`tmt try {{rhel-9}}`

- Select both custom image and provision method:

`tmt try {{fedora@container}}`

- Select tests with custom filter:

`tmt try {{[-t|--test]}} {{feature}}`

- Provision guest and wait for instructions:

`tmt try {{[-a|--ask]}}`

- Directly log into the guest without asking:

`tmt try {{[-l|--login]}}`

- Display help:

`tmt try --help`
