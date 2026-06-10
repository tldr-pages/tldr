# coproc

> Bash-ը ներկառուցված է ինտերակտիվ ասինխրոն ենթաշերտեր ստեղծելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>:.

- Գործարկել ենթաշելլը ասինխրոն կերպով.:

`coproc { {{command1; command2; ...}}; }`

- Ստեղծեք համատեղ գործընթաց հատուկ անունով.:

`coproc {{name}} { {{command1; command2; ...}}; }`

- Գրեք կոնկրետ համատեղ գործընթացի `stdin`:

`echo "{{input}}" >&"${{{name[1]}}}"`

- Կարդացեք կոնկրետ համատեղ գործընթացից `stdout`:

`read <&"${{{name[0]}}}" {{variable}}`

- Ստեղծեք համատեղ պրոցես, որը բազմիցս կարդում է `stdin` և գործարկում է որոշ հրամաններ մուտքագրման վրա.:

`coproc {{name}} { while read {{line}}; do {{command1; command2; ...}}; done }`

- Ստեղծեք համատեղ գործընթաց, որը բազմիցս կարդում է `stdin`, խողովակաշար է անցնում մուտքի վրա և ելքը գրում `stdout`-ում:

`coproc {{name}} { while read {{line}}; do {{echo "$line"}} | {{command1 | command2 | ...}} | cat /dev/fd/0; done }`

- Ստեղծեք և օգտագործեք համատեղ գործընթաց, որն աշխատում է `bc`:

`coproc BC { bc {{[-l|--mathlib]}}; }; echo "1/3" >&"${BC[1]}"; read <&"${BC[0]}" output; echo "$output"`
