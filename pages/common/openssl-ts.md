# openssl ts

> OpenSSL command to generate and verify timestamps.
> More information: <https://www.openssl.org/docs/manmaster/man1/openssl-ts.html>.

- Generate a SHA-512 timestamp request of `file` (output to `file.tsq`):

`openssl ts -query -data {{path/to/file}}  -sha512  -out {{path/to/file.tsq}}`

- Check the date and metadata of a specific timestamp response file:

`openssl ts -reply -in {{path/to/file.tsr}} -text`

- Verify timestamp request `file.tsq` and timestamp response `file.tsr` from the server with ssl certificate `cert.pem`:

`openssl ts -verify -in {{path/to/file.tsr}} -queryfile {{path/to/file.tsq}} -partial_chain -CAfile {{path/to/cert.pem}}`

- Create a timestamp response for request `file.tsq` using key `tsakey.pem` and signing certificate `tsacert.pem` (output to `file.tsr`):

`openssl ts -reply -queryfile {{path/to/file.tsq}} -inkey {{path/to/tsakey.pem}} -signer tsacert.pem -out {{path/to/file.tsr}}`
