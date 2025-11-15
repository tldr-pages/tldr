# zsync

> Partial/differential file downloader.
> HTTPS is not supported - use HTTP URLs only.
> See also: `rsync`.
> More information: <https://manned.org/zsync>.

- Download a file using a `.zsync` control file:

`zsync {{path/to/url.zsync}}`

- Use a local file as a seed to avoid re-downloading unchanged parts:

`zsync -i {{path/to/existing_file}} {{path/to/url.zsync}}`

- Save the updated file under a specific name:

`zsync -i {{path/to/existing_file}} -o {{path/to/new_file}} {{path/to/url.zsync}}`

- Resume a partial download and keep the temporary file:

`zsync -k {{path/to/url.zsync}}`

- Run in quiet mode with minimal output (no progress bar, download rate, or ETA display):

`zsync -q {{path/to/url.zsync}}`
