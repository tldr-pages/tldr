# bats

> Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash.
> More information: <https://github.com/bats-core/bats-core>.

- Run a BATS test script and output results in the TAP (Test Anything Protocol) format:

`bats --tap {{path/to/test.bats}}`

- Count test cases without running any tests in the test script:

`bats --count {{path/to/test.bats}}`

- Run BATS test cases contained in a directory and subdirectories with file extension `.bats`:

`bats --recursive {{path/to/directory}}`

- Output results in a specific format:

`bats --formatter {{pretty|tap|junit}} {{path/to/test.bats}}`
