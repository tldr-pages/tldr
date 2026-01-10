# apptainer sign

> Add digital signatures to a SIF container image.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_sign.html>.

- Sign a container image using the default PGP key:

`apptainer sign {{path/to/image.sif}}`

- Sign a container image using a specific private key file:

`apptainer sign --key {{path/to/private.pem}} {{path/to/image.sif}}`

- Sign a container image using a specific PGP key index:

`apptainer sign {{[-k|--keyidx]}} {{key_index}} {{path/to/image.sif}}`

- Sign a specific object group within the image:

`apptainer sign {{[-g|--group-id]}} {{group_id}} {{path/to/image.sif}}`

- Sign a specific object by ID within the image:

`apptainer sign {{[-i|--sif-id]}} {{object_id}} {{path/to/image.sif}}`

- Display help:

`apptainer sign {{[-h|--help]}}`
