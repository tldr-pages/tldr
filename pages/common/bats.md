# bats

> Bash Automated Testing System is a TAP (https://testanything.org/) compliant testing framework for Bash.
> More information: <https://github.com/bats-core/bats-core>.

- Run BATS tests in test script and output results in TAP (Test Anything Protocol) format:

`bats --tap {{path/to/test.bats}}`

- Count test cases without running any tests in the test script:

`bats --count {{path/to/test.bats}}`

- Run BATS tests in test scripts of a directory and subdirectories with file extension `.bats`:

`bats --recursive {{path/to/directory}}`

- Run BATS tests in test script and output results in desired format:

`bats --formatter {{pretty|tap|junit}} {{path/to/test.bats}}`
