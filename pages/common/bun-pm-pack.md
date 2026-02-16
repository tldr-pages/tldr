# bun pm pack

> Create a `.tgz` archive containing the files that would be published to npm (same behavior as `npm pack`).
> More information: <https://bun.com/docs/pm/cli/pm#pack>.

- Create a tarball from the current workspace:

`bun pm pack`

- Run all steps without writing the tarball to disk:

`bun pm pack --dry-run`

- Save the tarball to a specific directory:

`bun pm pack --destination {{path/to/directory}}`

- Set an exact filename for the tarball:

`bun pm pack --filename {{filename}}`

- Skip prepack, postpack, and prepare scripts:

`bun pm pack --ignore-scripts`

- Set the gzip compression level (0-9, default: 9):

`bun pm pack --gzip-level 5`

- Output only the tarball filename and suppress verbose logs:

`bun pm pack --quiet`
