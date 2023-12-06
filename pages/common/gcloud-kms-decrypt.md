# gcloud kms decrypt

> Decrypt a ciphertext file using a Cloud KMS key.
> More information: <https://cloud.google.com/sdk/gcloud/reference/kms/decrypt>.

- Decrypt a file using a specified key, key ring, and location:

`gcloud kms decrypt --key=frodo --keyring=fellowship --location=global --ciphertext-file=path/to/input/ciphertext --plaintext-file=path/to/output/plaintext.dec`

- Decrypt a file with additional authenticated data (AAD) and write the decrypted plaintext to stdout:

`gcloud kms decrypt --key=frodo --keyring=fellowship --location=global --additional-authenticated-data-file=path/to/aad --ciphertext-file=path/to/input/ciphertext --plaintext-file=-`

---

**Note:** Ensure that you have the necessary permissions and roles (e.g., roles/cloudkms.cryptoKeyDecrypter, roles/cloudkms.cryptoKeyEncrypterDecrypter) for decryption. The `--skip-integrity-verification` flag can be used to disable integrity verification if needed.
