# BaiduPCS-GO

> A Baidu Netdisk CLI client.
> Supports uploading, downloading, saving shared files, and offline downloading.
> More information: <https://github.com/qjfoidnh/BaiduPCS-Go>.

- Log in to a Baidu Netdisk account using BDUSS and STOKEN (see <https://github.com/qjfoidnh/BaiduPCS-Go#登录百度帐号> for instructions on obtaining them):

`BaiduPCS-GO login -bduss {{bduss}} -stoken {{stoken}}`

- Download remote files or directories to a specific local directory (downloads to `./download/` if `--saveto` is omitted):

`BaiduPCS-GO download {{path/to/remote1 path/to/remote2 ...}} --saveto {{path/to/local_directory}}`

- Upload local files or directories to a remote directory:

`BaiduPCS-GO upload {{path/to/local1 path/to/local2 ...}} {{path/to/remote_directory}}`

- Save files from a shared link to the remote working directory:

`BaiduPCS-GO transfer {{share_url}} {{access_code}}`

- Change the remote working directory:

`BaiduPCS-GO cd {{path/to/remote_directory}}`

- List files and directories in a remote directory:

`BaiduPCS-GO ls {{path/to/remote_directory}}`

- Start an interactive session:

`BaiduPCS-GO`
