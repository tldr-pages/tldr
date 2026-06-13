# apx subsystems

> Manage subsystems in `apx`.
> Subsystems are containers that can be created based on pre-existing stacks.
> More information: <https://docs.vanillaos.org/docs/en/apx-manpage#subsystems>.

- Interactively create a new subsystem:

`apx subsystems new`

- List all available subsystems:

`apx subsystems list`

- Reset a specific subsystem to its initial state:

`apx subsystems reset {{[-n|--name]}} {{string}}`

- Force reset a specific subsystem:

`apx subsystems reset {{[-n|--name]}} {{string}} {{[-f|--force]}}`

- Remove a specific subsystem:

`apx subsystems rm {{[-n|--name]}} {{string}}`

- Force remove a specific subsystem:

`apx subsystems rm {{[-n|--name]}} {{string}} {{[-f|--force]}}`
