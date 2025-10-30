# tmt

> Test Management Tool for creating, running, and debugging tests.
> Some subcommands such as `run`, `try`, etc. have their own usage documentation.
> More information: <https://tmt.readthedocs.io>.

- List available tests, plans, and stories:

`tmt`

- Initialize tmt files/project structure:

`tmt init`

- Create a new test with a template and a link:

`tmt test create {{[-t|--template]}} {{beakerlib}} --link {{verifies:issue#1234}}`

- List available tests, plans, or stories:

`tmt {{test|plan|story}} ls {{pattern}}`

- Show detailed test metadata in the given context:

`tmt {{[-c|--context]}} {{arch=aarch64}} test show`

- Validate tmt files against the specification:

`tmt lint`

- Use filter:

`tmt tests ls {{[-f|--filter]}} {{tag:foo}} {{[-f|--filter]}} {{tier:0}}`

- Display help:

`tmt --help`
