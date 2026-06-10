# վեբհեղեղ

> WebTorrent-ի ինտերֆեյսը:.
> Աջակցում է մագնիսներին, URL-ներին, տեղեկատվության հեշերին և `.torrent` ֆայլերին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/webtorrent/webtorrent-cli>:.

- Ներբեռնեք հեղեղ.:

`webtorrent download "{{torrent_id}}"`

- Ուղարկեք հեղեղ VLC մեդիա նվագարկիչ.:

`webtorrent download "{{torrent_id}}" --vlc`

- Հեռարձակեք հեղեղ դեպի Digital Living Network Alliance (DLNA) սարք.:

`webtorrent download "{{torrent_id}}" --dlna`

- Ցուցադրել ֆայլերի ցանկը կոնկրետ հեղեղի համար.:

`webtorrent download "{{torrent_id}}" --select`

- Ներբեռնելու համար նշեք ֆայլի ինդեքսը հեղեղից.:

`webtorrent download "{{torrent_id}}" --select {{index}}`

- Սերմնացրեք որոշակի ֆայլ կամ գրացուցակ.:

`webtorrent seed {{path/to/file_or_directory}}`

- Ստեղծեք նոր torrent ֆայլ նշված ֆայլի ուղու համար.:

`webtorrent create {{path/to/file}}`

- Ցուցադրել տեղեկատվություն մագնիսական URI-ի կամ `.torrent` ֆայլի համար.:

`webtorrent info {{path/to/file_or_magnet}}`
