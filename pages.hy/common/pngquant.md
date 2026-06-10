# pngquant

> PNG փոխարկիչ և կորուստ ունեցող պատկերի կոմպրեսոր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pngquant>:.

- Որքան հնարավոր է սեղմեք կոնկրետ PNG և գրեք արդյունքը նոր ֆայլում.:

`pngquant {{path/to/file.png}}`

- Սեղմեք որոշակի PNG և անտեսեք բնօրինակը.:

`pngquant --ext .png {{[-f|--force]}} {{path/to/file.png}}`

- Փորձեք սեղմել որոշակի PNG հատուկ որակով (բաց թողնել, եթե նվազագույն արժեքից ցածր է).:

`pngquant {{[-Q|--quality]}} {{0-100}} {{path/to/file.png}}`

- Սեղմեք որոշակի PNG գույների քանակով կրճատված մինչև 64:

`pngquant {{64}} {{path/to/file.png}}`

- Սեղմեք որոշակի PNG և բաց թողեք, եթե ֆայլն ավելի մեծ է, քան բնօրինակը:

`pngquant --skip-if-larger {{path/to/file.png}}`

- Սեղմեք որոշակի PNG և հեռացրեք մետատվյալները.:

`pngquant --strip {{path/to/file.png}}`

- Սեղմեք որոշակի PNG և պահեք այն տրված ճանապարհին.:

`pngquant {{path/to/file.png}} {{[-o|--output]}} {{path/to/file.png}}`

- Սեղմեք որոշակի PNG և ցույց տվեք առաջընթացը.:

`pngquant {{[-v|--verbose]}} {{path/to/file.png}}`
