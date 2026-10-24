# BaiduPCS-Go

> A Baidu Netdisk CLI client.
> Supports uploading, downloading, saving shared files, and offline downloading.
> More information: <https://github.com/qjfoidnh/BaiduPCS-Go>.

- Log in to a Baidu Netdisk account using BDUSS and STOKEN (see <https://github.com/qjfoidnh/BaiduPCS-Go#%E7%99%BB%E5%BD%95%E7%99%BE%E5%BA%A6%E5%B8%90%E5%8F%B7>):

`BaiduPCS-Go login -bduss {{bduss}} -stoken {{stoken}}`

- Download remote files or directories to a specific local directory (downloads to `./download/` if `--saveto` is omitted):

`BaiduPCS-Go download {{path/to/remote1 path/to/remote2 ...}} --saveto {{path/to/local_directory}}`

- Upload local files or directories to a remote directory:

`BaiduPCS-Go upload {{path/to/local1 path/to/local2 ...}} {{path/to/remote_directory}}`

- Save files from a shared link to the remote working directory:

`BaiduPCS-Go transfer {{share_url}} {{access_code}}`

- Change the remote working directory:

`BaiduPCS-Go cd {{path/to/remote_directory}}`

- List files and directories in a remote directory:

`BaiduPCS-Go ls {{path/to/remote_directory}}`

- Start an interactive session:

`BaiduPCS-Go`
