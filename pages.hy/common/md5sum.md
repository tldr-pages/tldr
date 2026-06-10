# md5sum

> Հաշվարկել MD5 ծածկագրային ստուգման գումարները:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>:.

- Հաշվեք MD5 ստուգիչ գումարը մեկ կամ մի քանի ֆայլերի համար.:

`md5sum {{path/to/file1 path/to/file2 ...}}`

- Հաշվեք և պահեք MD5 ստուգումների ցուցակը ֆայլում.:

`md5sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.md5}}`

- Հաշվեք MD5 ստուգիչ գումարը `stdin`-ից:

`{{command}} | md5sum`

- Կարդացեք MD5 ստուգիչ գումարների և ֆայլերի անունների ֆայլը և ստուգեք, որ բոլոր ֆայլերն ունեն համապատասխան ստուգման գումարներ.:

`md5sum {{[-c|--check]}} {{path/to/file.md5}}`

- Ցուցադրել հաղորդագրություն միայն բացակայող ֆայլերի համար կամ երբ ստուգումը ձախողվում է.:

`md5sum {{[-c|--check]}} --quiet {{path/to/file.md5}}`

- Ցուցադրել հաղորդագրություն միայն այն դեպքում, երբ ստուգումը ձախողվում է՝ անտեսելով բացակայող ֆայլերը.:

`md5sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.md5}}`

- Ստուգեք ֆայլի հայտնի MD5 ստուգիչ գումարը.:

`echo {{known_md5_checksum_of_the_file}} {{path/to/file}} | md5sum {{[-c|--check]}}`
