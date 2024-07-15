# gdown

> Сommand-line tool to download files from Google Drive and other URLs.
> Install: `pip install gdown`.
> More information: <https://github.com/wkentaro/gdown>.

- Download a file from a URL:

`gdown https://drive.google.com/uc?id={{FILE_ID}}`

- Download using file ID:

`gdown {{FILE_ID}}`

- Download with fuzzy file ID extraction (also works with `docs.google.com` links):

`gdown --fuzzy '{{URL}}'`

- Download a folder:

`gdown https://drive.google.com/drive/folders/{{FOLDER_ID}} -O {{/tmp/folder}} --folder`

- Write stdout and pipe to extract:

`gdown https://github.com/wkentaro/gdown/archive/refs/tags/v4.0.0.tar.gz -O - --quiet | tar zxvf -`

- Maxi Command (Most options example): Download folder from https://drive.google.com/drive/folders/FOLDER_ID with [fuzzy] extraction of the file ID from the URL,
using a specified [proxy] server, cookies disabled, SSL certificate check skipped, resuming partially downloaded files,
ignoring any missing files within the folder, specifying the output directory, and suppressing output messages for a quieter download process.

`gdown --fuzzy --proxy "http://proxy.example.com:8080" --no-cookies --no-check-certificate --continue --folder --remaining-ok "https://drive.google.com/drive/folders/FOLDER_ID" -O /tmp/folder --quiet`
