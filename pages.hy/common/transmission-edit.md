# փոխանցում-խմբագրում

> Փոփոխել անոնսի URL-ները torrent ֆայլերից:.
> Տես նաև՝ `transmission`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/transmission-edit>:.

- Ավելացնել URL հեղեղի հայտարարությունների ցանկում.:

`transmission-edit {{[-a|--add]}} {{http://example.com}} {{path/to/file.torrent}}`

- Հեռացրեք URL-ը torrent-ի հայտարարությունների ցանկից.:

`transmission-edit {{[-d|--delete]}} {{http://example.com}} {{path/to/file.torrent}}`

- Թարմացրեք թրեյքերի ծածկագիրը torrent ֆայլում.:

`transmission-edit {{[-r|--replace]}} {{old-passcode}} {{new-passcode}} {{path/to/file.torrent}}`
