# sha512sum

> Հաշվարկել SHA512 ծածկագրային ստուգաչափերը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>:.

- Հաշվեք SHA512 ստուգիչ գումարը մեկ կամ մի քանի ֆայլերի համար.:

`sha512sum {{path/to/file1 path/to/file2 ...}}`

- Հաշվեք և պահեք SHA512 ստուգիչ գումարների ցանկը ֆայլում.:

`sha512sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha512}}`

- Հաշվեք SHA512 ստուգիչ գումարը `stdin`-ից:

`{{command}} | sha512sum`

- Կարդացեք SHA512 ստուգիչ գումարների և ֆայլերի անունների ֆայլը և ստուգեք, որ բոլոր ֆայլերը ունեն համապատասխան ստուգման գումարներ.:

`sha512sum {{[-c|--check]}} {{path/to/file.sha512}}`

- Ցուցադրել հաղորդագրություն միայն բացակայող ֆայլերի համար կամ երբ ստուգումը ձախողվում է.:

`sha512sum {{[-c|--check]}} --quiet {{path/to/file.sha512}}`

- Ցուցադրել հաղորդագրություն միայն այն դեպքում, երբ ստուգումը ձախողվում է՝ անտեսելով բացակայող ֆայլերը.:

`sha512sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha512}}`

- Ստուգեք ֆայլի հայտնի SHA512 ստուգիչ գումարը.:

`echo {{known_sha512_checksum_of_the_file}} {{path/to/file}} | sha512sum {{[-c|--check]}}`
