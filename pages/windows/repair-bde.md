# repair-bde

> Attempt to repair or decrypt a damaged BitLocker-encrypted volume.

- Attempt to repair a specified volume:

`repair-bde {{C:}}`

- Attempt to repair a specified volume and output to another volume:

`repair-bde {{C:}} {{D:}}`

- Attempt to repair a specified volume using the provided recovery key file:

`repair-bde {{C:}} -RecoveryKey {{path/to/file.bek}}`

- Attempt to repair a specified volume using the provided numerical recovery password:

`repair-bde {{C:}} -RecoveryPassword {{password}}`

- Attempt to repair a specified volume using the provided password:

`repair-bde {{C:}} -Password {{password}}`

- Attempt to repair a specified volume using the provided key package:

`repair-bde {{C:}} -KeyPackage {{path/to/directory}}`

- Log all output to a specific file:

`repair-bde {{C:}} -LogFile {{path/to/file}}`

- Display all available options:

`repair-bde /?`
