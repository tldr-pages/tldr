# b4 am

> Retrieve and prepare patches from a public-inbox archive for applying with `git am`.
> More information: <https://b4.docs.kernel.org/en/latest/maintainer/am-shazam.html>.

- Retrieve patches from a thread and prepare them for `git am`:

`b4 am {{message_id}}`

- Retrieve patches and add your own `Signed-off-by` trailer as well as a `Link:` trailer to every commit:

`b4 am {{[-sl|--add-my-sob --add-link]}} {{message_id}}`

- Retrieve patches and prepare with 3-way merge support for conflict resolution:

`b4 am {{[-3|--prep-3way]}} {{message_id}}`

- Cherry-pick a subset of patches (e.g., patches 1-3 and 5) from a series:

`b4 am {{[-P|--cherry-pick]}} {{1-3,5}} {{message_id}}`

- Retrieve patches and run local checks on each patch:

`b4 am --check {{message_id}}`

- Save the output mailbox to a specific directory:

`b4 am {{[-o|--outdir]}} {{path/to/directory}} {{message_id}}`
