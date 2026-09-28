# jj converge

> Converge divergent changes.
> Attempts to resolve divergence by replacing two or more visible revisions for a given change with a single revision.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-converge>.

- Converge divergent revisions in the default search space (configured by `revsets.converge`):

`jj converge`

- Converge divergent revisions within a specific search space:

`jj converge {{[-r|--revision]}} {{revset}}`

- Resolve divergence without interactive prompts:

`jj converge --no-interactive`
