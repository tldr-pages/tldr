# repair-bde

> Attempt to repair or decrypt a damaged BitLocker-encrypted volume.

- Attempt to repair a specified volume:

`repair-bde {{input_volume}}`

- Attempt to repair a specified volume and output to another volume:

`repair-bde {{input_volume}} {{output_volume}}`

- Attempt to repair a specified volume using the provided recovery key file:

`repair-bde {{input_volume}} -RecoveryKey {{path/to/file.bek}}`

- Attempt to repair a specified volume using the provided numerical recovery password:

`repair-bde {{input_volume}} -RecoveryPassword {{password}}`

- Attempt to repair a specified volume using the provided password:

`repair-bde {{input_volume}} -Password {{password}}`

- Attempt to repair a specified volume using the provided key package:

`repair-bde {{input_volume}} -KeyPackage {{path/to/directory}}`

- Log all output to a specific file:

`repair-bde {{input_volume}} -LogFile {{path/to/file}}`

- Display all available options:

`repair-bde /?`
