# apptainer verify

> Verify digital signatures of SIF container images.
> See also: `apptainer-sign`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_verify.html>.

- Verify a container image using the default PGP keyring:

`apptainer verify {{path/to/image.sif}}`

- Verify a container image using a specific public key file:

`apptainer verify --key {{path/to/public.pem}} {{path/to/image.sif}}`

- Verify a container image using a certificate file:

`apptainer verify --certificate {{path/to/certificate.pem}} {{path/to/image.sif}}`

- Verify all objects in the image:

`apptainer verify {{[-a|--all]}} {{path/to/image.sif}}`

- Verify a specific object group within the image:

`apptainer verify {{[-g|--group-id]}} {{group_id}} {{path/to/image.sif}}`

- Verify a specific object by ID within the image:

`apptainer verify {{[-i|--sif-id]}} {{object_id}} {{path/to/image.sif}}`

- Output verification results in JSON format:

`apptainer verify {{[-j|--json]}} {{path/to/image.sif}}`

- Display help:

`apptainer verify {{[-h|--help]}}`
