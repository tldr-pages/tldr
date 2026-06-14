#դյուֆ

> Սկավառակի օգտագործում/անվճար կոմունալ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/muesli/duf#usage>:.

- Ցուցակեք մատչելի սարքերը.:

`duf`

- Թվարկեք ամեն ինչ (օրինակ՝ կեղծ, կրկնօրինակ կամ անհասանելի ֆայլային համակարգեր).:

`duf --all`

- Ցուցադրել միայն նշված սարքերը կամ ամրացման կետերը.:

`duf {{path/to/directory1 path/to/directory2 ...}}`

- Տեսակավորել ելքը ըստ սահմանված չափանիշների.:

`duf --sort {{size|used|avail|usage}}`

- Ցույց տալ կամ թաքցնել որոշակի ֆայլային համակարգեր.:

`duf --{{only-fs|hide-fs}} {{tmpfs|vfat|ext4|xfs}}`

- Տեսակավորել ելքը ըստ բանալիի.:

`duf --sort {{mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem}}`

- Փոխեք թեման (եթե `duf`-ը չի կարողանում օգտագործել ճիշտ թեման).:

`duf --theme {{dark|light}}`
