# zsync

> Partial/differential file downloader.
> Efficiently updates large files over HTTP by transferring only changed blocks using a `.zsync` control file.
> Similar to `rsync`, but designed for HTTP and file mirroring.
> HTTPS is not supported - use HTTP URLs only.
> More information: <http://zsync.moria.org.uk>.

- Download a file using a `.zsync` control file:

`zsync {{url.zsync}}`

- Use a local file as a seed to avoid re-downloading unchanged parts:

`zsync -i {{existing_file_path}} {{url.zsync}}`

- Save the updated file under a specific name:

`zsync -i {{existing_file_path}} -o {{new_file_path}} {{url.zsync}}`

- Resume a partial download and keep the temporary file:

`zsync -k {{url.zsync}}`

- Run in quiet mode with minimal output (no progress bar, download rate, or ETA display):

`zsync -q {{url.zsync}}`
