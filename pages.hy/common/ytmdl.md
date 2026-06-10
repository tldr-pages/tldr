# ytmdl

> Ներբեռնեք երգեր YouTube-ից և ավտոմատ կերպով ավելացրեք մետատվյալներ:.
> Ստացեք երգի մասին տեղեկատվություն (արտիստ, ալբոմ, շապիկ) iTunes-ից, Spotify-ից և այլ աղբյուրներից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/deepjyoti30/ytmdl#usage>:.

- Ներբեռնեք երգ անունով (ինտերակտիվ ընտրությամբ).:

`ytmdl {{song_name}}`

- Ներբեռնեք առաջին արդյունքը առանց հուշելու.:

`ytmdl {{[-q|--quiet]}} {{song_name}}`

- Ներբեռնեք երգը որոշակի գրացուցակում.:

`ytmdl {{[-o|--output-dir]}} {{path/to/directory}} {{song_name}}`

- Ներբեռնեք երգ YouTube URL-ից.:

`ytmdl --url https://www.youtube.com/watch?v={{oHg5SJYRHA0}}`

- Ներբեռնեք երգ կոնկրետ ձևաչափով (mp3, m4a կամ opus):

`ytmdl --format {{mp3|m4a|opus}} {{song_name}}`

- Ներբեռնեք երգ նկարչի և ալբոմի տեղեկություններով.:

`ytmdl --artist {{artist_name}} --album {{album_name}} {{song_name}}`

- Ներբեռնեք երգերի ցանկը տեքստային ֆայլից.:

`ytmdl --list {{path/to/list.txt}}`

- Ցուցադրել օգնությունը.:

`ytmdl {{[-h|--help]}}`
