# sha224sum

> Հաշվարկել SHA224 ծածկագրային ստուգաչափերը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>:.

- Հաշվեք SHA224 ստուգիչ գումարը մեկ կամ մի քանի ֆայլերի համար.:

`sha224sum {{path/to/file1 path/to/file2 ...}}`

- Հաշվեք և պահեք SHA224 ստուգիչ գումարների ցանկը ֆայլում.:

`sha224sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha224}}`

- Հաշվեք SHA224 ստուգիչ գումարը `stdin`-ից:

`{{command}} | sha224sum`

- Կարդացեք SHA224 ստուգիչ գումարների և ֆայլերի անունների ֆայլը և ստուգեք, որ բոլոր ֆայլերն ունեն համապատասխան ստուգման գումարներ.:

`sha224sum {{[-c|--check]}} {{path/to/file.sha224}}`

- Ցուցադրել հաղորդագրություն միայն բացակայող ֆայլերի համար կամ երբ ստուգումը ձախողվում է.:

`sha224sum {{[-c|--check]}} --quiet {{path/to/file.sha224}}`

- Ցուցադրել հաղորդագրություն միայն այն դեպքում, երբ ստուգումը ձախողվում է՝ անտեսելով բացակայող ֆայլերը.:

`sha224sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha224}}`

- Ստուգեք ֆայլի հայտնի SHA224 ստուգիչ գումարը.:

`echo {{known_sha224_checksum_of_the_file}} {{path/to/file}} | sha224sum {{[-c|--check]}}`
