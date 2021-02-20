# pueue add

> Enqueue a task for execution.
> More information: <https://github.com/Nukesor/pueue>.

- Add any command to the default queue:

`pueue add {{command}}`

- Pass flags or arguments to command when adding:

`pueue add -- {{command --Arg -f}}`

- Add command but do not start it if it's the first in a queue:

`pueue add --stashed -- rsync -az /local/directory/ /remote/directory/`

- Add command to a [g]roup and start it [i]mmmediately, see "tldr pueue-group" to operate groups:

`pueue add -ig "CPU_intensive" -- ffmpeg -i input.mp4 frame_%d.png`

- Add command and start it [a]fter commands 9 and 12 finish successfully:

`pueue add -a 9 12 -g "torrents" -- transmission-cli {{torrent_file}}.torrent`

- Add command with a [l]abel after some [d]elay has passed, see "pueue enqueue --help" for valid datetime formats:

`pueue add -l "compressing large file" -d "wednesday 10:30pm" "7z a compressed_file.7z large_file.xml"`
