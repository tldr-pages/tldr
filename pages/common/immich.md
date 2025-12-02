# immich

> Manage Immich servers.
> See also: `immich-go`.
> More information: <https://immich.app/docs/features/command-line-interface/>.

- Authenticate to Immich server:

`immich login {{server_url/api}} {{server_key}}`

- Upload some image files:

`immich upload {{file1.jpg file2.jpg ...}}`

- Upload a directory including subdirectories:

`immich upload {{[-r|--recursive]}} {{path/to/directory}}`

- Create an album based on a directory:

`immich upload {{[-r|--recursive]}} {{path/to/directory}} {{[-A|--album-name]}} "{{My summer holiday}}"`

- Skip assets matching a glob pattern:

`immich upload {{[-r|--recursive]}} {{path/to/directory}} {{[-i|--ignore]}} {{**/Raw/** **/*.tif}}`

- Include hidden files:

`immich upload {{[-r|--recursive]}} {{path/to/directory}} {{[-H|--include-hidden]}}`
