# բազմանցում

> Կառավարեք Ubuntu-ի վիրտուալ մեքենաները՝ օգտագործելով բնիկ հիպերվիզորներ:.
> Լրացուցիչ տեղեկություններ. <https://documentation.ubuntu.com/multipass/latest/reference/command-line-interface/>:.

- Թվարկեք այն անունները, որոնք կարող են օգտագործվել օրինակ գործարկելու համար.:

`multipass find`

- Գործարկեք նոր օրինակ, սահմանեք դրա անունը և օգտագործեք cloud-init կազմաձևման ֆայլ.:

`multipass launch {{[-n|--name]}} {{instance_name}} --cloud-init {{configuration_file}}`

- Թվարկեք ստեղծված բոլոր օրինակները և դրանց որոշ հատկություններ.:

`multipass list`

- Սկսեք կոնկրետ օրինակ անունով.:

`multipass start {{instance_name}}`

- Ցույց տալ օրինակի հատկությունները.:

`multipass info {{instance_name}}`

- Բացեք կեղևի հուշում կոնկրետ օրինակի վրա անունով.:

`multipass shell {{instance_name}}`

- Ջնջել օրինակը անունով.:

`multipass delete {{instance_name}}`

- Տեղադրեք գրացուցակը որոշակի օրինակի մեջ.:

`multipass mount {{path/to/local_directory}} {{instance_name}}:{{path/to/target_directory}}`
