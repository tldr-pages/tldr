# tmt

> Test Management Tool for creating, running and debugging tests.
> See also: `tmt-run`, `tmt-try`.
> More information: <https://tmt.readthedocs.io>.

- Look around to see what's available:

`tmt`

- Initialize tmt files/project structure:

`tmt init`

- Create a new test with template and link:

`tmt test create --template {{beakerlib}} --link {{verifies:issue#1234}}`

- List available tests, plans, or stories:

`tmt <test|plan|story> ls {{pattern}}`

- Show detailed test metadata in the given context:

`tmt --context {{arch=aarch64}} test show`

- Validate tmt files against the specification:

`tmt lint`

- Use filter:

`tmt tests ls --filter {{tag:foo}} --filter {{tier:0}}`

- Display help:

`tmt --help`
