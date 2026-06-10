# pip կազմաձևում

> Կառավարեք տեղական և գլոբալ կոնֆիգուրացիան pip-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://pip.pypa.io/en/stable/cli/pip_config/>:.

- Նշեք բոլոր կազմաձևման արժեքները.:

`pip config list`

- Ցուցադրել կազմաձևման ֆայլերը և դրանց արժեքները.:

`pip config debug`

- Սահմանեք հրամանի ընտրանքի արժեքը.:

`pip config set {{command.option}} {{value}} {{--global|--user|--site}}`

- Ստացեք հրամանի տարբերակի արժեքը.:

`pip config get {{command.option}} {{--global|--user|--site}}`

- Անջատեք հրամանի ընտրանքի արժեքը.:

`pip config unset {{command.option}} {{--global|--user|--site}}`

- Խմբագրեք կազմաձևման ֆայլը լռելյայն խմբագրիչով.:

`pip config edit {{--global|--user|--site}}`

- Խմբագրեք կազմաձևման ֆայլը հատուկ խմբագրիչով.:

`pip config edit {{--global|--user|--site}} --editor {{path/to/editor_binary}}`
