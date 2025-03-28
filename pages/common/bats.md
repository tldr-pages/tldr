# bats

> Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash.
> More information: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Run a BATS test script and output results in the TAP (Test Anything Protocol) format:

`bats {{[-t|--tap]}} {{path/to/test.bats}}`

- Count test cases of a test script without running any tests:

`bats {{[-c|--count]}} {{path/to/test.bats}}`

- Run BATS test cases recursively (files with a `.bats` extension):

`bats {{[-r|--recursive]}} {{path/to/directory}}`

- Output results in a specific format:

`bats {{[-F|--formatter]}} {{pretty|tap|tap13|junit}} {{path/to/test.bats}}`

- Add timing information to tests:

`bats {{[-T|--timing]}} {{path/to/test.bats}}`

- Run specific number of jobs in parallel (requires GNU `parallel` to be installed):

`bats {{[-j|--jobs]}} {{number}} {{path/to/test.bats}}`
