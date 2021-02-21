# pueue add

> Enqueue a task for execution.
> More information: <https://github.com/Nukesor/pueue>.

- Add any command to the default queue:

`pueue add {{command}}`

- Pass flags or arguments to command when adding:

`pueue add -- {{command --arg -f}}`

- Add command but do not start it if it's the first in a queue:

`pueue add --stashed -- {{rsync --archive --compress /local/directory /remote/directory}}`

- Add command to a group and start it immmediately, see `pueue group` to manage groups:

`pueue add --immediate --group "{{CPU_intensive}}" -- {{ffmpeg -i input.mp4 frame_%d.png}}`

- Add command and start it after commands 9 and 12 finish successfully:

`pueue add --after {{9}} {{12}} --group "{{torrents}}" -- {{transmission-cli torrent_file.torrent}}`

- Add command with a label after some delay has passed, see `pueue enqueue` for valid datetime formats:

`pueue add --label "{{compressing large file}}" --delay "{{wednesday 10:30pm}}" -- "{{7z a compressed_file.7z large_file.xml}}"`
