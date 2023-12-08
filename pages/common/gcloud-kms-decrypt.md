# gcloud kms decrypt

> Decrypt a ciphertext file using a Cloud KMS key.
> See also: `gcloud`.
> More information: <https://cloud.google.com/sdk/gcloud/reference/kms/decrypt>.

- Decrypt a file using a specified key, key ring, and location:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{global}} --ciphertext-file={{path/to/ciphertext}} --plaintext-file={{path/to/plaintext}}`

- Decrypt a file with additional authenticated data (AAD) and write the decrypted plaintext to `stdout`:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{global}} --additional-authenticated-data-file={{path/to/file.aad}} --ciphertext-file={{path/to/ciphertext}} --plaintext-file=-`
