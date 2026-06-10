#այլևս

> Վերցրեք տիրույթի URL-ները Wayback Machine-ից, Common Crawl-ից, Alien Vault OTX-ից, URLScan-ից և VirusTotal-ից:.
> Նշում. Եթե նշված չէ, ելքը թափվում է `results/` գրացուցակում, որտեղ գտնվում է waymore-ի `config.yml`-ը (կանխադրված՝ `~/.config/waymore/`-ում):.
> Լրացուցիչ տեղեկություններ. <https://github.com/xnl-h4ck3r/waymore>:.

- Որոնեք տիրույթի URL-ներ (ելքը սովորաբար կլինի `~/.config/waymore/results/`-ով):

`waymore {{[-i|--input]}} {{example.com}}`

- Սահմանափակեք որոնման արդյունքները՝ ներառելով միայն տիրույթի URL-ների ցանկը և պահեք ելքերը նշված ֆայլում.:

`waymore -mode U {{[-oU|--output-urls]}} {{path/to/example.com-urls.txt}} {{[-i|--input]}} {{example.com}}`

- Արտադրեք միայն URL-ների բովանդակության մարմինները և պահեք ելքերը նշված գրացուցակում.:

`waymore -mode R {{[-oR|--output-responses]}} {{path/to/example.com-url-responses}} {{[-i|--input]}} {{example.com}}`

- Զտեք արդյունքները՝ նշելով ամսաթվերի միջակայքերը.:

`waymore -from {{YYYYMMDD|YYYYMM|YYYY}} {{[-to|--to-date]}} {{YYYYMMDD|YYYYMM|YYYY}} {{[-i|--input]}} {{example.com}}`
