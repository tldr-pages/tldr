# immich-cli

> Immich has a command line interface (CLI) that allows you to perform certain actions from the command line.
> See also: `immich-go`.
> More information: <https://immich.app/docs/features/command-line-interface/>.

- Authenticate to Immich server:

`immich login {{server_url/api}} {{server_key}}`

- Upload some image files:

`immich upload {{file1.jpg file2.jpg}}`

- Upload a directory including subdirectories:

`immich upload --recursive {{path/to/directory}}`

- Create an album based on a directory:

`immich upload --album-name "{{My summer holiday}}" --recursive {{path/to/directory}}`

- Skip assets matching a glob pattern:

`immich upload --ignore {{**/Raw/** **/*.tif}} --recursive {{path/to/directory}}`

- Include hidden files:

`immich upload --include-hidden --recursive {{path/to/directory}}`
