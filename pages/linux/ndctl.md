# ndctl

> Utility for managing Non-Volatile DIMMs.
> More information: <https://manned.org/ndctl>.

- Create an 'fsdax' mode namespace:

`ndctl create-namespace --mode={{fsdax}}`

- Change the mode of a namespace to 'raw':

`ndctl create-namespace --reconfigure={{namespaceX.Y}} --mode={{raw}}`

- Check a sector mode namespace for consistency, and repair if needed:

`ndctl check-namespace --repair {{namespaceX.Y}}`

- List all namespaces, regions, and buses (including disabled ones):

`ndctl list --namespaces --regions --buses --idle`

- List a specific namespace and include lots of additional information:

`ndctl list -vvv --namespace={{namespaceX.Y}}`

- Run a monitor to watch for SMART health events for NVDIMMs on the 'ACPI.NFIT' bus:

`ndctl monitor --bus={{ACPI.NFIT}}`

- Remove a namespace (when applicable) or reset it to an initial state:

`ndctl destroy-namespace --force {{namespaceX.Y}}`
