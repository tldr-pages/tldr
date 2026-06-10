# getArch.py

> Որոշեք OS ճարտարապետությունը (x86 կամ x64) հեռավոր Windows համակարգի:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Ստուգեք մեկ թիրախային համակարգի ճարտարապետությունը.:

`getArch.py -target {{target}}`

- Ստուգեք մի քանի թիրախների ճարտարապետությունը ֆայլից (մեկ տողում).:

`getArch.py -targets {{path/to/targets_file}}`

- Սահմանեք հատուկ վարդակից ժամանակի ավարտ (կանխադրվածը 2 վայրկյան է).:

`getArch.py -target {{target}} -timeout {{seconds}}`

- Միացնել վրիպազերծման ռեժիմը մանրամասն արդյունքի համար.:

`getArch.py -target {{target}} -debug`
