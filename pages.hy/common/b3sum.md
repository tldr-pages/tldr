# b3sum

> Հաշվարկել BLAKE3 ծածկագրային ստուգման գումարները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>:.

- Հաշվեք BLAKE3 ստուգիչ գումարը մեկ կամ մի քանի ֆայլերի համար.:

`b3sum {{path/to/file1 path/to/file2 ...}}`

- Հաշվեք և պահեք BLAKE3 ստուգիչ գումարների ցանկը ֆայլում.:

`b3sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.b3}}`

- Հաշվեք BLAKE3 ստուգիչ գումարը `stdin`-ից:

`{{command}} | b3sum`

- Կարդացեք BLAKE3 ստուգիչ գումարների և ֆայլերի անունների ֆայլը և ստուգեք, որ բոլոր ֆայլերն ունեն համապատասխան ստուգման գումարներ.:

`b3sum {{[-c|--check]}} {{path/to/file.b3}}`

- Ցուցադրել հաղորդագրություն միայն բացակայող ֆայլերի համար կամ երբ ստուգումը ձախողվում է.:

`b3sum {{[-c|--check]}} --quiet {{path/to/file.b3}}`

- Ստուգեք ֆայլի հայտնի BLAKE3 ստուգիչ գումարը.:

`echo {{known_blake3_checksum_of_the_file}} {{path/to/file}} | b3sum {{[-c|--check]}}`
