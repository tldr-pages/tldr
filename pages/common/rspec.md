# rspec

> Behavior-driven development testing framework written in Ruby to test Ruby code.
> More information: <https://rspec.info>.

- Initialize an .rspec configuration and a spec helper file:

`rspec --init`

- Run all tests:

`rspec`

- Run a specific directory of tests:

`rspec {{path/to/directory}}`

- Run one or more test files:

`rspec {{path/to/file1 path/to/file2 ...}}`

- Run a specific test in a file (e.g. the test starts on line 83):

`rspec {{path/to/file}}:{{83}}`

- Run specs with a specific seed:

`rspec --seed {{seed_number}}`
