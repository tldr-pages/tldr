# BaiduPCS-Go

> A Baidu Netdisk client.
> Upload, download, save shared files, and perform cloud downloading.
> More information: <https://github.com/qjfoidnh/BaiduPCS-Go>.

- Log in to a Baidu Netdisk account using BDUSS and STOKEN:

`BaiduPCS-Go login --bduss {{bduss}} --stoken {{stoken}}`

- Download remote files or directories to a specific local directory (downloads to `./download/` if `--saveto` is omitted):

`BaiduPCS-Go download {{path/to/remote_file_or_directory1 path/to/remote_file_or_directory2 ...}} --saveto {{path/to/local_directory}}`

- Upload local files or directories to a remote directory:

`BaiduPCS-Go upload {{path/to/local_file_or_directory1 path/to/local_file_or_directory2 ...}} {{path/to/remote_directory}}`

- Save files from a shared link to the remote working directory:

`BaiduPCS-Go transfer {{share_url}} {{access_code}}`

- Change the remote working directory:

`BaiduPCS-Go cd {{path/to/remote_directory}}`

- List files and directories in a remote directory:

`BaiduPCS-Go ls {{path/to/remote_directory}}`

- Start an interactive session:

`BaiduPCS-Go`
