# dexdump

> Display information about Android DEX files.

- Extract classes and methods from an APK file:

`dexdump {{path/to/file.apk}}`

- Display DEX files header information:

`dexdump -f {{path/to/file.apk}}`

- Display the dis-assembled output of executable sections:

`dexdump -d {{path/to/file.apk}}`

- Output results to a file:

`dexdump -o {{path/to/file}} {{path/to/file.apk}}`
