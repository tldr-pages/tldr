# tarsnap-keygen

> Generate a key file for use with Tarsnap, an online backup service.
> More information: <https://www.tarsnap.com/man-tarsnap-keygen.1.html>.

- Register a machine with the Tarsnap server:

`sudo tarsnap-keygen --keyfile {{path/to/file.key}} --user {{user_email}} --machine {{machine_name}}`

- Encrypt the key file (a passphrase will be requested twice):

`sudo tarsnap-keygen --keyfile {{path/to/file.key}} --user {{user_email}} --machine {{machine_name}} --passphrased`
