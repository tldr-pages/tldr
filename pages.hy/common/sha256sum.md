# sha256sum

> Հաշվարկել SHA256 ծածկագրային ստուգաչափերը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>:.

- Հաշվեք SHA256 ստուգիչ գումարը մեկ կամ մի քանի ֆայլերի համար.:

`sha256sum {{path/to/file1 path/to/file2 ...}}`

- Հաշվեք և պահեք SHA256 ստուգիչ գումարների ցանկը ֆայլում.:

`sha256sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha256}}`

- Հաշվեք SHA256 ստուգիչ գումարը `stdin`-ից:

`{{command}} | sha256sum`

- Կարդացեք SHA256 ստուգիչ գումարների և ֆայլերի անունների ֆայլը և ստուգեք, որ բոլոր ֆայլերն ունեն համապատասխան ստուգման գումարներ.:

`sha256sum {{[-c|--check]}} {{path/to/file.sha256}}`

- Ցուցադրել հաղորդագրություն միայն բացակայող ֆայլերի համար կամ երբ ստուգումը ձախողվում է.:

`sha256sum {{[-c|--check]}} --quiet {{path/to/file.sha256}}`

- Ցուցադրել հաղորդագրություն միայն այն դեպքում, երբ ստուգումը ձախողվում է՝ անտեսելով բացակայող ֆայլերը.:

`sha256sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha256}}`

- Ստուգեք ֆայլի հայտնի SHA256 ստուգիչ գումարը.:

`echo {{known_sha256_checksum_of_the_file}} {{path/to/file}} | sha256sum {{[-c|--check]}}`
