# netperf

> Հաճախորդի կողմից հրաման `netperf`-ի համար՝ համեմատական հավելված, որը չափում է ցանցի թողունակությունը: Նման է `iperf`-ին:.
> Տես նաև՝ `netserver`:.
> Լրացուցիչ տեղեկություններ. <https://hewlettpackard.github.io/netperf/doc/netperf.html#Global-Command_002dline-Options>:.

- Միացեք սերվերին որոշակի IP հասցեով լռելյայն պորտի միջոցով (12865):

`netperf {{address}}`

- Նշեք [p]ort:

`netperf {{address}} -p {{port}}`

- Նշեք նմուշառման [l] երկարությունը վայրկյաններով (կանխադրվածը 10 է).:

`netperf {{address}} -l {{seconds}}`

- Ստիպել IPv[4] կամ IPv[6]:

`netperf {{address}} -{{4|6}}`
