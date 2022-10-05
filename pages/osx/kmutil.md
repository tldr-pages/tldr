# kmutil

> Utility for managing kernel extensions (kexts) and kext collections on disk.
> More information: <https://keith.github.io/xcode-man-pages/kmutil.8.html>.

- Find kexts available on the operating system:

`kmutil find`

- Display logging information about the Kernel Management sub-system:

`kmutil log`

- Inspect and display a kext collection's contents according to the options provided:

`kmutil inspect {{options}}`

- Check the consistency of kext collections against each other:

`kmutil check`

- Dump kernelmanagerd state for debugging:

`sudo kmutil dumpstate`

- Load one or more extensions based on the bundle specified at this path in the results:

`kmutil load --bundle-path {{path/to/extension.kext}}`
