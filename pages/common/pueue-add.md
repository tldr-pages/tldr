# pueue add

> Enqueue a task for execution.
> More information: <https://github.com/Nukesor/pueue#how-to-use-it>.

- Add any command to the default queue:

`pueue add {{command}}`

- Pass a list of flags or arguments to a command when enqueuing:

`pueue add -- {{command --arg -f}}`

- Add a command but do not start it if it's the first in a queue:

`pueue add {{[-s|--stashed]}} -- {{rsync --archive --compress /local/directory /remote/directory}}`

- Add a command to a group and start it immediately, see `pueue group` to manage groups:

`pueue add {{[-i|--immediate]}} {{[-g|--group]}} "{{CPU_intensive}}" -- {{ffmpeg -i input.mp4 frame_%d.png}}`

- Add a command and start it after commands 9 and 12 finish successfully:

`pueue add {{[-a|--after]}} {{9}} {{12}} {{[-g|--group]}} "{{torrents}}" -- {{transmission-cli torrent_file.torrent}}`

- Add a command with a label after some delay has passed, see `pueue enqueue` for valid datetime formats:

`pueue add {{[-l|--label]}} "{{compressing large file}}" {{[-d|--delay]}} "{{wednesday 10:30pm}}" -- "{{7z a compressed_file.7z large_file.xml}}"`
