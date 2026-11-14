# forge

> Build, test, fuzz, debug, and deploy Solidity smart contracts.
> Note: Not to be confused with the unrelated Laravel Forge and Atlassian Forge CLIs, which also provide a `forge` command.
> Part of Foundry.
> See also: `hardhat`.
> More information: <https://getfoundry.sh/reference/forge/forge>.

- Create a new project in a specific directory:

`forge init {{path/to/directory}}`

- Compile the project's contracts:

`forge build`

- Run all tests and print execution traces for failing tests:

`forge test -vvv`

- Run only the tests whose function names match a `regex`:

`forge test --match-test {{regex}}`

- Run a deployment script and broadcast its transactions using a keystore account:

`forge script {{path/to/script.s.sol}} --rpc-url {{rpc_url}} --account {{keystore_name}} --broadcast`

- Save a gas usage snapshot of every test to `.gas-snapshot`:

`forge snapshot`

- Format the project's Solidity files:

`forge fmt`

- Install a dependency from a GitHub repository:

`forge install {{owner}}/{{repository}}`
