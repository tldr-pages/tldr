# cli53

> Գործիք Amazon Route 53-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/barnybug/cli53>:.

- Ցուցակեք տիրույթները.:

`cli53 list`

- Ստեղծեք տիրույթ.:

`cli53 create {{example.com}} --comment "{{comment}}"`

- Արտահանել bind zone ֆայլը `stdout`:

`cli53 export {{example.com}}`

- Ստեղծեք `www` ենթադոմեյն՝ մատնանշելով հարաբերական գրառումը նույն գոտում.:

`cli53 {{[rc|rrcreate]}} {{example.com}} '{{www 300 CNAME lb}}'`

- Ստեղծեք `www` ենթադոմեյն՝ մատնանշելով արտաքին հասցե (պետք է ավարտվի կետով).:

`cli53 {{[rc|rrcreate]}} {{example.com}} '{{www 300 CNAME lb.example.com.}}'`

- Ստեղծեք `www` ենթադոմեյն՝ մատնանշելով IP հասցե.:

`cli53 {{[rc|rrcreate]}} {{example.com}} '{{www 300 A 150.130.110.1}}'`

- Փոխարինեք `www` ենթադոմեյնը՝ մատնանշելով այլ IP.:

`cli53 {{[rc|rrcreate]}} --replace '{{www 300 A 150.130.110.2}}'`

- Ջնջել գրառումը A:

`cli53 {{[rd|rrdelete]}} {{example.com}} {{www}} {{A}}`
