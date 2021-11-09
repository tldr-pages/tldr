# http-server-upload

> Zero-configuration command-line HTTP server which provides a lightweight interface to upload files.
> More information: <https://github.com/crycode-de/http-server-upload>.

- Start an HTTP server on the default port to upload files to the current directory:

`http-server-upload`

- Start an HTTP server with the specified maximum allowed file size for uploads in MiB (defaults to 200 MiB):

`MAX_FILE_SIZE={{size_in_megabytes}} http-server-upload`

- Start an HTTP server on a specific port to upload files to the current directory:

`PORT={{port}} http-server-upload`

- Start an HTTP server, storing the uploaded files in a specific directory:

`UPLOAD_DIR={{path/to/directory}} http-server-upload`

- Start an HTTP server using a specific directory to temporarily store files during the upload process:

`UPLOAD_TMP_DIR={{path/to/directory}} http-server-upload`

- Start an HTTP server accepting uploads with a specific token field in the HTTP post:

`TOKEN={{secret}} http-server-upload`
