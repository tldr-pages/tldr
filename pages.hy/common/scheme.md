# սխեմա

> MIT Scheme լեզվի թարգմանիչ և REPL (ինտերակտիվ կեղև):.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/mit-scheme/documentation/stable/mit-scheme-user.html#Command_002dLine-Options>:.

- Սկսեք REPL (ինտերակտիվ կեղև).:

`scheme`

- Գործարկել սխեմայի ծրագիր (առանց REPL ելքի).:

`scheme < {{script.scm}} --quiet`

- Բեռնել սխեմայի ծրագիր REPL-ում.:

`scheme --load {{script.scm}}`

- Բեռնել սխեմայի արտահայտությունները REPL-ում.:

`scheme --eval "{{(define foo 'x)}}"`

- Բացեք REPL-ը հանգիստ ռեժիմով.:

`scheme --quiet`
