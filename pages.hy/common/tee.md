#թեյ

> Կարդացեք `stdin`-ից և գրեք `stdout`-ին և ֆայլերին (կամ հրամաններին):.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>:.

- Պատճենեք `stdin` յուրաքանչյուր ֆայլ, ինչպես նաև `stdout`:

`echo "example" | tee {{path/to/file}}`

- Կցեք տրված ֆայլերին, մի վերագրեք.:

`echo "example" | tee {{[-a|--append]}} {{path/to/file}}`

- Տպեք `stdin`-ը տերմինալում, ինչպես նաև այն տեղափոխեք մեկ այլ ծրագիր՝ հետագա մշակման համար.:

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Ստեղծեք «example» անունով գրացուցակ, հաշվեք «example»-ի նիշերի քանակը և տերմինալում գրեք «example».:

`echo "example" | tee >(xargs mkdir) >(wc {{[-c|--bytes]}})`
