# bats

> Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash.
> More information: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Run a BATS test script and output results in the TAP (Test Anything Protocol) format:

`bats --tap {{path/to/test.bats}}`

- Count test cases of a test script without running any tests:

`bats --count {{path/to/test.bats}}`

- Run BATS test cases contained in a directory and its subdirectories (files with a `.bats` extension):

`bats --recursive {{path/to/directory}}`

- Output results in a specific format:

`bats --formatter {{pretty|tap|junit}} {{path/to/test.bats}}`
