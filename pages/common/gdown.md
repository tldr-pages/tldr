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

`gdown {{folder_id|url}} -O {{path/to/output_directory}} --folder`

- Write stdout and pipe to extract:

`gdown https://github.com/wkentaro/gdown/archive/refs/tags/v4.0.0.tar.gz -O - --quiet | tar zxvf -`
