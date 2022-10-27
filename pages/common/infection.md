# infection

> A mutation testing framework for PHP.
> More information: <https://infection.github.io>.

- Analyze code using the configuration file (or create one if it does not exist):

`infection`

- Use a specific number of threads:

`infection --threads {{number_of_threads}}`

- Specify a minimum Mutation Score Indicator (MSI):

`infection --min-msi {{percentage}}`

- Specify a minimum covered code MSI:

`infection --min-covered-msi {{percentage}}`

- Use a specific test framework (defaults to PHPUnit):

`infection --test-framework {{phpunit|phpspec}}`

- Only mutate lines of code that are covered by tests:

`infection --only-covered`

- Display the mutation code that has been applied:

`infection --show-mutations`

- Specify the log verbosity:

`infection --log-verbosity {{default|all|none}}`
