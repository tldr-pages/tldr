# kubectx

> Utility to manage and switch between `kubectl` contexts.
> More information: <https://manned.org/kubectx>.

- List the contexts:

`kubectx`

- Switch to a named context:

`kubectx {{name}}`

- Switch to the previous context:

`kubectx -`

- Rename a named context:

`kubectx {{alias}}={{name}}`

- Show the current named context:

`kubectx {{[-c|--current]}}`

- Delete a named context:

`kubectx -d {{name}}`
