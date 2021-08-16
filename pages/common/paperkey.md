# paperkey

> An OpenPGP key archiver.
> More information: <https://www.jabberwocky.com/software/paperkey/>.

- Take the secret key in `secret_key.gpg` and generate a text file `secret_data.txt` that contains the secret data:

`paperkey --secret-key {{path/to/secret_key.gpg}} --output {{path/to/secret_data.txt}}`

- Take the secret key data in `secret_data.txt` and combine it with `public_key.gpg` to reconstruct `secret_key.gpg`:

`paperkey --pubring {{path/to/public_key.gpg}} --secrets {{path/to/secret_data.txt}} --output {{secret_key.gpg}}`

- Export the secret key `my-key`, generate a text file to be printed, and send it to the default printer:

`gpg --export-secret-key {{my-key}} | paperkey | lpr`
