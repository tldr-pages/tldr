# dircolors

> Ելք հրամաններ՝ `$LS_COLOR` միջավայրի փոփոխականը և ոճը սահմանելու համար `ls`, `dir` և այլն:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>:.

- Արտադրեք հրամաններ՝ `$LS_COLOR` սահմանելու համար՝ օգտագործելով լռելյայն գույները.:

`dircolors`

- Ցուցադրել յուրաքանչյուր ֆայլի տեսակը գույնով, որը նրանք կհայտնվեն `ls`-ում:

`dircolors --print-ls-colors`

- Արտադրեք հրամաններ՝ `$LS_COLOR` սահմանելու համար՝ օգտագործելով գույները ֆայլից.:

`dircolors {{path/to/file}}`

- Արդյունք հրամաններ Bourne shell-ի համար.:

`dircolors {{[-b|--bourne-shell]}}`

- Ելքային հրամաններ C shell-ի համար.:

`dircolors {{[-c|--c-shell]}}`

- Դիտեք լռելյայն գույները ֆայլերի տեսակների և ընդարձակման համար.:

`dircolors {{[-p|--print-database]}}`
