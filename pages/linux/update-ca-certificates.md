# update-ca-certificates

> Update the CA certificates bundle and regenerate `/etc/ssl/certs`.
> More information: <https://manned.org/update-ca-certificates>.

- Update certificates:

`sudo update-ca-certificates`

- Update certificates, being [v]erbose:

`sudo update-ca-certificates {{[-v|--verbose]}}`

- Perform a [f]resh update (remove all symlinks and regenerate):

`sudo update-ca-certificates {{[-f|--fresh]}}`

- Add a custom certificate (copy it first, then update):

`sudo cp {{path/to/certificate.crt}} /usr/local/share/ca-certificates/ && sudo update-ca-certificates`
