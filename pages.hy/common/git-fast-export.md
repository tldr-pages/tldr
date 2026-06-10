# git արագ արտահանում

> Արտահանել Git պահոցի բովանդակությունը և պատմությունը հոսքային, պարզ տեքստի ձևաչափով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/git-fast-export>:.

- Արտահանել ամբողջ Git պահեստի պատմությունը `stdout`:

`git fast-export --all`

- Արտահանել ամբողջ պահեստը ֆայլ.:

`git fast-export --all > {{path/to/file}}`

- Արտահանել միայն կոնկրետ մասնաճյուղ.:

`git fast-export {{main}}`

- Արտահանել `progress` հայտարարություններով յուրաքանչյուր `n` օբյեկտ (`git fast-import`-ի ընթացքում առաջընթաց ցույց տալու համար):

`git fast-export --progress {{n}} --all > {{path/to/file}}`

- Արտահանել միայն կոնկրետ ենթագրքի պատմությունը.:

`git fast-export --all -- {{path/to/directory}} > {{path/to/file}}`
