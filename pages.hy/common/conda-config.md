# conda config

> Փոփոխել կազմաձևման արժեքները `.condarc`-ում:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/config.html>:.

- Ցուցադրել բոլոր կազմաձևման արժեքները.:

`conda config --show`

- Ցույց տալ կազմաձևման ընտրանքի ընթացիկ արժեքը.:

`conda config --show {{config_option}}`

- Սահմանեք կազմաձևման արժեքը.:

`conda config --set {{key}} {{value}}`

- Հեռացրեք կազմաձևման արժեքը.:

`conda config --remove {{key}} {{value}}`

- Կազմաձևման բանալիների ցանկին արժեք ավելացրեք.:

`conda config --append {{key}} {{value}}`

- Գոյություն ունեցող կազմաձևման ստեղների ցանկին արժեք ներկայացրեք.:

`conda config --prepend {{key}} {{value}}`

- Նկարագրեք տվյալ կազմաձևման տարբերակը.:

`conda config --describe {{config_option}}`
