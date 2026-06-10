# կռունկի ինդեքսի զտիչ

> Փոփոխում է հեռավոր ինդեքսը՝ զտելով՝ հիմնվելով հարթակի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>:.

- Փոփոխել հեռավոր ինդեքսը.:

`crane index filter`

- Նշեք հարթակ(ներ)ը, որոնք պետք է պահվեն բազայից `os/arch/variant:osversion,platform` ձևով.:

`crane index filter --platform {{platform1 platform2 ...}}`

- Ստացված պատկերին կիրառելու համար նշեք.:

`crane index filter {{[-t|--tags]}} {{tag_name}}`

- Ցուցադրել օգնությունը.:

`crane index filter {{[-h|--help]}}`
