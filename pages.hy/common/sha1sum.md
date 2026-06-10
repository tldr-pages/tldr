# sha1sum

> Հաշվարկել SHA1 ծածկագրային ստուգաչափերը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/sha1sum-invocation.html>:.

- Հաշվեք SHA1 ստուգման գումարը մեկ կամ մի քանի ֆայլերի համար.:

`sha1sum {{path/to/file1 path/to/file2 ...}}`

- Հաշվեք և պահեք SHA1 ստուգիչ գումարների ցանկը ֆայլում.:

`sha1sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha1}}`

- Հաշվեք SHA1 ստուգիչ գումարը `stdin`-ից:

`{{command}} | sha1sum`

- Կարդացեք SHA1 ստուգիչ գումարների և ֆայլերի անունների ֆայլը և ստուգեք, որ բոլոր ֆայլերն ունեն համապատասխան ստուգման գումարներ.:

`sha1sum {{[-c|--check]}} {{path/to/file.sha1}}`

- Ցուցադրել հաղորդագրություն միայն բացակայող ֆայլերի համար կամ երբ ստուգումը ձախողվում է.:

`sha1sum {{[-c|--check]}} --quiet {{path/to/file.sha1}}`

- Ցուցադրել հաղորդագրություն միայն այն դեպքում, երբ ստուգումը ձախողվում է՝ անտեսելով բացակայող ֆայլերը.:

`sha1sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha1}}`

- Ստուգեք ֆայլի հայտնի SHA1 ստուգիչ գումարը.:

`echo {{known_sha1_checksum_of_the_file}} {{path/to/file}} | sha1sum {{[-c|--check]}}`
