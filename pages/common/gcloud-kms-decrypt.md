# gcloud kms decrypt

> Decrypt a ciphertext file using a Cloud KMS key.
> Decrypts a given ciphertext file using a specified Cloud KMS key and writes the result to a plaintext file.
> More information: <https://cloud.google.com/sdk/gcloud/reference/kms/decrypt>.

- Decrypt a file using a specified key, keyring, and location, and write the plaintext to a file:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{location}} --ciphertext-file={{path/to/ciphertext_file}} --plaintext-file={{path/to/plaintext_file}}`

- Decrypt a file using additional authenticated data and write the plaintext to stdout:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{location}} --additional-authenticated-data-file={{path/to/additional_authenticated_data_file}} --ciphertext-file={{path/to/ciphertext_file}} --plaintext-file=-`

- Decrypt a file and skip integrity verification on data sent to and received from Cloud KMS:

`gcloud kms decrypt --skip-integrity-verification --key={{key_name}} --keyring={{keyring_name}} --location={{location}} --ciphertext-file={{path/to/ciphertext_file}} --plaintext-file={{path/to/plaintext_file}}`

- Decrypt a file using a specified key and read the ciphertext from stdin:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{location}} --ciphertext-file=- --plaintext-file={{path/to/plaintext_file}}`

- Decrypt a file using a key and output the plaintext directly to stdout:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{location}} --ciphertext-file={{path/to/ciphertext_file}} --plaintext-file=-`

- Decrypt a file using a specific key version:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{location}} --ciphertext-file={{path/to/ciphertext_file}} --plaintext-file={{path/to/plaintext_file}} --version={{key_version}}`

- Decrypt a file using the default key for the current project and location:

`gcloud kms decrypt --ciphertext-file={{path/to/ciphertext_file}} --plaintext-file={{path/to/plaintext_file}}`

- Decrypt a file using a key, specifying a project and location:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{location}} --project={{project_id}} --ciphertext-file={{path/to/ciphertext_file}} --plaintext-file={{path/to/plaintext_file}}`
