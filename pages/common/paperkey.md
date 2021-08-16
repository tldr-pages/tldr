# paperkey

> An OpenPGP key archiver.
> More information: <https://www.jabberwocky.com/software/paperkey/>.

- Take the secret key in `secret-key.gpg` and generate a text file `to-be-printed.txt` that contains the secret data:

`paperkey --secret-key {{secret-key.gpg}} --output {{to-be-printed.txt}}`

- Take the secret key data in {{secret-key.txt}} and combine it with {{public-key.gpg}} to reconstruct {{secret-key.gpg}}:

`paperkey --pubring {{my-public-key.gpg}} --secrets {{secret-key.txt}} --output {{secret-key.gpg}}`

- Export the secret key `my-key`, generate a text file to be printed, and send it to the default printer:

`gpg --export-secret-key {{my-key}} | paperkey | lpr`
