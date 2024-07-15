# gdown

> Download files from Google Drive and other URLs.
> More information: <https://github.com/wkentaro/gdown>.

- Download a file from a URL:

`gdown {{url}}`

- Download using a file ID:

`gdown {{file_id}}`

- Download with fuzzy file ID extraction (also works with <https://docs.google.com> links):

`gdown --fuzzy {{url}}`

- Download a folder:

`gdown https://drive.google.com/drive/folders/{{FOLDER_ID}} -O {{/tmp/folder}} --folder`

- Write stdout and pipe to extract:

`gdown https://github.com/wkentaro/gdown/archive/refs/tags/v4.0.0.tar.gz -O - --quiet | tar zxvf -`

- Maxi Command (Most options example):

`gdown --fuzzy --proxy "http://proxy.example.com:8080" --no-cookies --no-check-certificate --continue --folder --remaining-ok "https://drive.google.com/drive/folders/FOLDER_ID" -O /tmp/folder --quiet`
