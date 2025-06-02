# zsync

> Partial/differential file downloader.
> Efficiently updates large files over HTTP by transferring only changed blocks using a `.zsync` control file.
> Similar to `rsync`, but designed for HTTP and file mirroring.
> All URLs must be HTTP only - HTTPS is not supported.
> More information: <http://zsync.moria.org.uk>.

- Download a file using a `.zsync` control file:

`zsync {{url}}`

- Use a local file as a seed to avoid re-downloading unchanged parts:

`zsync -i {{existing-file-path}} {{url}}`

- Save the updated file under a specific name:

`zsync -i {{existing-file-path}} -o {{new-file-path}} {{url}}`

- Resume a partial download and keep the temporary file:

`zsync -k {{url}}`

- Use a previously downloaded `.zsync` file with a base URL for relative paths:

`zsync -u {{url}} {{Packages.zsync}}`

- Run in quiet mode with minimal output (no progress bar, download rate, or ETA display):

`zsync -q {{url}}`
