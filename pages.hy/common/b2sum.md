# b2sum

> Հաշվարկել BLAKE2 ծածկագրային ստուգումների գումարները:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>:.

- Հաշվեք BLAKE2 ստուգիչ գումարը մեկ կամ մի քանի ֆայլերի համար.:

`b2sum {{path/to/file1 path/to/file2 ...}}`

- Հաշվեք և պահեք BLAKE2 ստուգիչ գումարների ցանկը ֆայլում.:

`b2sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file}}.b2`

- Հաշվեք BLAKE2 ստուգիչ գումարը `stdin`-ից:

`{{command}} | b2sum`

- Կարդացեք BLAKE2 ստուգիչ գումարների և ֆայլերի անունների ֆայլը և ստուգեք, որ բոլոր ֆայլերն ունեն համապատասխան ստուգման գումարներ.:

`b2sum {{[-c|--check]}} {{path/to/file}}.b2`

- Ցուցադրել հաղորդագրություն միայն բացակայող ֆայլերի համար կամ երբ ստուգումը ձախողվում է.:

`b2sum {{[-c|--check]}} --quiet {{path/to/file}}.b2`

- Ցուցադրել հաղորդագրություն միայն այն դեպքում, երբ ստուգումը ձախողվում է՝ անտեսելով բացակայող ֆայլերը.:

`b2sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file}}.b2`

- Ստուգեք ֆայլի հայտնի BLAKE2 ստուգիչ գումարը.:

`echo {{known_blake2_checksum_of_the_file}} {{path/to/file}} | b2sum {{[-c|--check]}}`
