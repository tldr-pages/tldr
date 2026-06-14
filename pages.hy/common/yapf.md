# yapf

> Python ոճի ուղեցույցի ստուգիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/yapf#usage>:.

- Ցուցադրել կատարված փոփոխությունների տարբերությունը՝ առանց դրանք կատարելու (չոր գործարկում).:

`yapf {{[-d|--diff]}} {{path/to/file}}`

- Ռեկուրսիվ ձևաչափեք բոլոր Python ֆայլերը գրացուցակում, միաժամանակ.:

`yapf {{[-ri|--recursive --in-place]}} --style {{pep8}} {{[-p|--parallel]}} {{path/to/directory}}`
