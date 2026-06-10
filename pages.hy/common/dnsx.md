# dnsx

> Արագ և բազմաֆունկցիոնալ DNS գործիքակազմ՝ բազմաթիվ DNS հարցումներ գործարկելու համար:.
> Նշում. որոշ դեպքերում `dnsx`-ի մուտքագրումը պետք է փոխանցվի `stdin`-ով (խողովակ `|`):.
> Տես նաև՝ `dig`, `dog`, `dnstracer`:.
> Լրացուցիչ տեղեկություններ. <https://docs.projectdiscovery.io/opensource/dnsx/usage>:.

- Հարցրեք (ենթա)տիրույթի գրառումը և ցույց տվեք ստացված պատասխանը.:

`echo {{example.com}} | dnsx -a {{[-re|-resp]}}`

- Հարցրեք բոլոր DNS գրառումները (A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR, CAA):

`dnsx <<< {{example.com}} -recon {{[-re|-resp]}}`

- Հարցրեք DNS գրառումների որոշակի տեսակ.:

`echo {{example.com}} | dnsx {{[-re|-resp]}} -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- Միայն ելքային պատասխան (մի ցույց տվեք հարցվող տիրույթը կամ ենթադոմեյնը).:

`echo {{example.com}} | dnsx {{[-ro|-resp-only]}}`

- Ցուցադրել հարցման չմշակված պատասխանը, նշելով լուծիչներ, որոնք պետք է օգտագործեն և նորից փորձեն անհաջողությունների դեպքում.:

`echo {{example.com}} | dnsx -{{debug|raw}} {{[-r|-resolver]}} {{1.1.1.1,8.8.8.8,...}} -retry {{number}}`

- Դաժան ուժային DNS գրառումներ՝ օգտագործելով տեղապահ.:

`dnsx {{[-d|-domain]}} {{FUZZ.example.com}} {{[-w|-wordlist]}} {{path/to/wordlist.txt}} {{[-re|-resp]}}`

- Դաժան ուժային DNS գրառումներ տիրույթների և բառացանկերի ցանկից՝ ելք ավելացնելով առանց գունային կոդերի ֆայլի.:

`dnsx {{[-d|-domain]}} {{path/to/domain.txt}} {{[-w|-wordlist]}} {{path/to/wordlist.txt}} {{[-re|-resp]}} {{[-o|-output]}} {{path/to/output.txt}} {{[-nc|-no-color]}}`

- Քաղեք `CNAME` գրառումները տվյալ ենթադոմեյնների ցանկի համար՝ DNS հարցումները սահմանափակող արագությամբ վայրկյանում.:

`subfinder -silent {{[-d|-domain]}} {{example.com}} | dnsx -cname {{[-re|-resp]}} {{[-rl|-rate-limit]}} {{number}}`
