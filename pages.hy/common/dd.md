# օր

> Փոխակերպել և պատճենել ֆայլը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/dd.1p>:.

- Ստեղծեք bootable USB drive isohybrid ֆայլից (օրինակ՝ `archlinux-xxx.iso`) և ցույց տվեք առաջընթացը.:

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}} status=progress`

- Կլոնավորեք սկավառակը 4 ՄԲ բլոկի չափով մեկ այլ սկավառակի վրա և գրեք մինչև հրամանի ավարտը.:

`dd bs=4194304 conv=fsync if={{/dev/source_drive}} of={{/dev/dest_drive}}`

- Ստեղծեք ֆայլ հատուկ թվով պատահական բայթերով՝ օգտագործելով միջուկի պատահական դրայվերը.:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- Սկավառակի հաջորդական գրելու կատարողականը համեմատեք.:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{path/to/file_1GB}}`

- Ստեղծեք համակարգի կրկնօրինակում, պահեք այն IMG ֆայլում (կարելի է հետագայում վերականգնել՝ փոխանակելով `if`-ը և `of`-ը), և ցույց տվեք առաջընթացը՝:

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`
