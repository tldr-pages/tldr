#միանալ

> Միացրեք երկու տեսակավորված ֆայլերի տողերը ընդհանուր դաշտում:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html>:.

- Միացրեք երկու ֆայլ առաջին (կանխադրված) դաշտում.:

`join {{path/to/file1}} {{path/to/file2}}`

- Միացրեք երկու ֆայլ՝ օգտագործելով ստորակետը (բացատի փոխարեն) որպես դաշտի բաժանարար.:

`join -t ',' {{path/to/file1}} {{path/to/file2}}`

- Միացրեք file1-ի դաշտը3-ը file2-ի դաշտ1-ին:

`join -1 {{3}} -2 {{1}} {{path/to/file1}} {{path/to/file2}}`

- Ստեղծեք տող յուրաքանչյուր չզուգակցվող տողի համար file1-ի համար:

`join -a {{1}} {{path/to/file1}} {{path/to/file2}}`

- Միացեք ֆայլ `stdin`-ից՝:

`cat {{path/to/file1}} | join - {{path/to/file2}}`
