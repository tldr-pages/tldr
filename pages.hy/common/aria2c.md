# aria2c

> Արագ ներբեռնման կոմունալ:.
> Աջակցում է HTTP(S), FTP, SFTP, BitTorrent և Metalink:.
> Տես նաև՝ `axel`:.
> Լրացուցիչ տեղեկություններ. <https://aria2.github.io/manual/en/html/aria2c.html>:.

- Ներբեռնեք որոշակի URI ֆայլ.:

`aria2c "{{url}}"`

- Ներբեռնեք ֆայլ URI-ից հատուկ ելքային անունով.:

`aria2c {{[-o|--out]}} {{path/to/file}} "{{url}}"`

- Զուգահեռաբար ներբեռնեք բազմաթիվ տարբեր ֆայլեր.:

`aria2c {{[-Z|--force-sequential=true]}} {{"url1" "url2" ...}}`

- Ներբեռնեք նույն ֆայլը տարբեր հայելիներից և ստուգեք ներբեռնված ֆայլի ստուգման գումարը.:

`aria2c --checksum {{sha-256}}={{hash}} {{"url1" "url2" ...}}`

- Ներբեռնեք ֆայլում թվարկված URI-ները՝ զուգահեռ ներբեռնումների որոշակի քանակով.:

`aria2c {{[-i|--input-file]}} {{path/to/file}} {{[-j|--max-concurrent-downloads]}} {{number_of_downloads}}`

- Ներբեռնեք բազմաթիվ կապերով.:

`aria2c {{[-s|--split]}} {{number_of_connections}} "{{url}}"`

- FTP ներբեռնում օգտվողի անունով և գաղտնաբառով.:

`aria2c --ftp-user {{username}} --ftp-passwd {{password}} "{{url}}"`

- Սահմանափակել ներբեռնման արագությունը բայթ/վրկ.:

`aria2c --max-download-limit {{speed}} "{{url}}"`
