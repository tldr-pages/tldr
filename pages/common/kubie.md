# kubie

> Utility to switch between `kubectl` contexts and namespaces.
> More information: <https://github.com/sbstp/kubie>.

- Display a selectable menu of contexts:

`kubie ctx`

- Switch current shell to the given context:

`kubie ctx {{context}}`

- Switch current shell to the given namespace:

`kubie ns {{namespace}}`

- Switch current shell to the given context and namespace:

`kubie ctx {{context}} -n {{namespace}}`

- Execute a command in the given context and namespace, without spawning a shell:

`kubie exec {{context}} {{namespace}} {{command}}`

- Check the Kubernetes config files for issues:

`kubie lint`
