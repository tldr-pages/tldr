# transfer.sh

> Command line client for transfer.sh.
> More information: <https://github.com/dutchcoders/transfer.sh/>.

- Upload a file to transfer.sh and print its URL:

`curl --updload-file {{path/to/file}} https://transfer.sh/{{file_name}}`

- Upload a file to transfer.sh showing a progress bar:

`curl --progress-bar --updload-file {{path/to/file}} https://transfer.sh/{{file_name}}`

- Download a file from transfer.sh:

`curl https://transfer.sh/{{token}}/{{file_name}}`
