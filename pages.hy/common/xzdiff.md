# xzdiff

> Կանչում է `diff` ֆայլերը, որոնք սեղմված են `xz`, `lzma`, `gzip`, `bzip2`, `lzop` կամ `zstd`-ով:.
> Նշված բոլոր ընտրանքները փոխանցվում են անմիջապես `diff`-ին:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/xzdiff>:.

- Համեմատեք երկու ֆայլ.:

`xzdiff {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք երկու ֆայլ՝ կողք կողքի ցույց տալով տարբերությունները.:

`xzdiff --side-by-side {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք երկու ֆայլ և զեկուցեք միայն, որ դրանք տարբերվում են (առանց այլ մանրամասների).:

`xzdiff --brief {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք երկու ֆայլ և զեկուցեք, երբ ֆայլերը նույնն են.:

`xzdiff --report-identical-files {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք երկու ֆայլ՝ օգտագործելով էջանշված արդյունքները.:

`xzdiff --paginate {{path/to/file1}} {{path/to/file2}}`
