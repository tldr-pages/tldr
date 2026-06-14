# gcrane ls

> Նշեք պիտակները պահեստում:.
> Ավելի բարդ ձև, քան `crane ls`-ը, որը թույլ է տալիս ցուցակագրել պիտակներ, մանիֆեստներ և ենթապահոցներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>:.

- Թվարկեք պիտակները.:

`gcrane ls {{repository}}`

- Ձևաչափեք պատասխանը գրանցամատյանից որպես JSON.:

`gcrane ls {{repository}} --json`

- Արդյոք կրկնել պահեստների միջոցով.:

`gcrane ls {{repository}} {{[-r|--recursive]}}`

- Ցուցադրել օգնությունը.:

`gcrane ls {{[-h|--help]}}`
