# pueue ավելացնել

> Հերթագրեք առաջադրանքը կատարման համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Nukesor/pueue#how-to-use-it>:.

- Լռելյայն հերթում ավելացրեք ցանկացած հրաման.:

`pueue add {{command}}`

- Հերթագրելիս հրամանին փոխանցեք դրոշների կամ փաստարկների ցանկ.:

`pueue add -- {{command --arg -f}}`

- Ավելացրեք հրաման, բայց մի սկսեք այն, եթե այն առաջինն է հերթում.:

`pueue add {{[-s|--stashed]}} -- {{rsync --archive --compress /local/directory /remote/directory}}`

- Խմբին հրաման ավելացրեք և անմիջապես սկսեք այն, տես `pueue group` խմբերը կառավարելու համար.:

`pueue add {{[-i|--immediate]}} {{[-g|--group]}} "{{cpu_intensive}}" -- {{ffmpeg -i input.mp4 frame_%d.png}}`

- Ավելացրեք հրաման և սկսեք այն 9 և 12 հրամանները հաջողությամբ ավարտելուց հետո.:

`pueue add {{[-a|--after]}} {{9}} {{12}} {{[-g|--group]}} "{{torrents}}" -- {{transmission-cli torrent_file.torrent}}`

- Որոշ ուշացումից հետո պիտակով հրաման ավելացրեք, տես `pueue enqueue` ամսաթվի վավեր ձևաչափերը.:

`pueue add {{[-l|--label]}} "{{compressing large file}}" {{[-d|--delay]}} "{{wednesday 10:30pm}}" -- "{{7z a compressed_file.7z large_file.xml}}"`
