# bats

> Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash.
> More information: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Run a BATS test script and output results in the [t]AP (Test Anything Protocol) format:

`bats --tap {{path/to/test.bats}}`

- [c]ount test cases of a test script without running any tests:

`bats --count {{path/to/test.bats}}`

- Run BATS test cases [r]ecursively (files with a `.bats` extension):

`bats --recursive {{path/to/directory}}`

- Output results in a specific [F]ormat:

`bats --formatter {{pretty|tap|tap13|junit}} {{path/to/test.bats}}`

- Add [T]iming information to tests:

`bats --timing {{path/to/test.bats}}`

- Run specific number of [j]obs in parallel (requires GNU `parallel` to be installed):

`bats --jobs {{number}} {{path/to/test.bats}}`
