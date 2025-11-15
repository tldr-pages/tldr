# gdown

> Download files from Google Drive and other URLs.
> More information: <https://github.com/wkentaro/gdown>.

- Download a file from a URL:

`gdown {{url}}`

- Download using a file ID:

`gdown {{file_id}}`

- Download with fuzzy file ID extraction (also works with <https://docs.google.com> links):

`gdown --fuzzy {{url}}`

- Download a folder using its ID or the full URL:

`gdown {{folder_id|url}} {{[-O|--output]}} {{path/to/output_directory}} --folder`

- Download a tar archive, write it to `stdout` and extract it:

`gdown {{tar_url}} {{[-O|--output]}} - {{[-q|--quiet]}} | tar xvf -`
