# jj պիտակը ջնջել

> Ջնջել պիտակները `jj` պահոցում:.
> Տես նաև՝ `jj tag list`, `jj tag set`:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag-delete>:.

- Ջնջել պիտակը.:

`jj tag {{[d|delete]}} {{tag_name}}`

- Ջնջել բազմաթիվ պիտակներ.:

`jj tag {{[d|delete]}} {{tag1 tag2 ...}}`

- Ջնջել գլոբալ օրինաչափությանը համապատասխանող պիտակները.:

`jj tag {{[d|delete]}} "{{glob:v1.*}}"`

- Ջնջել ենթալարի օրինակին համապատասխանող պիտակները.:

`jj tag {{[d|delete]}} "{{substring:release}}"`

- Ջնջել պիտակը ճշգրիտ անունով.:

`jj tag {{[d|delete]}} "{{exact:v1.0.0}}"`
