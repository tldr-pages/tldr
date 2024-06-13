# kubectx

> Utility to manage and switch between `kubectl` contexts.
> More information: <https://github.com/ahmetb/kubectx>.

- List the contexts:

`kubectx`

- Switch to a named context:

`kubectx {{name}}`

- Switch to the previous context:

`kubectx -`

- Rename a named context:

`kubectx {{alias}}={{name}}`

- Show the current named context:

`kubectx -c`

- Delete a named context:

`kubectx -d {{name}}`
