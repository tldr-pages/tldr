#գաու

> Ստացեք բոլոր URL-ները. բերեք հայտնի URL-ներ AlienVault-ի Open Threat Exchange-ից, Wayback Machine-ից և Common Crawl-ից ցանկացած տիրույթի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/lc/gau#usage>:.

- Վերցրեք տիրույթի բոլոր URL-ները AlienVault-ի Open Threat Exchange-ից, Wayback Machine-ից, Common Crawl-ից և URLScan-ից:

`gau {{example.com}}`

- Ստացեք բազմաթիվ տիրույթների URL-ներ.:

`gau {{domain1 domain2 ...}}`

- Ներառեք մի քանի տիրույթների բոլոր URL-ները մուտքային ֆայլից, որոնք աշխատում են բազմաթիվ թելերով.:

`gau < {{path/to/domains.txt}} --threads {{4}}`

- Գրեք [o]utput արդյունքները ֆայլում.:

`gau {{example.com}} --o {{path/to/found_urls.txt}}`

- Որոնեք URL-ներ միայն մեկ կոնկրետ մատակարարից.:

`gau --providers {{wayback|commoncrawl|otx|urlscan}} {{example.com}}`

- Որոնեք URL-ներ բազմաթիվ մատակարարներից.:

`gau --providers {{wayback,otx,...}} {{example.com}}`

- Որոնեք URL-ներ կոնկրետ ամսաթվերի միջակայքում.:

`gau --from {{YYYYMM}} --to {{YYYYMM}} {{example.com}}`
