# pulumi կոնֆիգուրացիա

> Կառավարեք Pulumi կույտի կազմաձևումը:.
> Լրացուցիչ տեղեկություններ. <https://www.pulumi.com/docs/iac/cli/commands/pulumi_config/>:.

- Դիտեք ընթացիկ կոնֆիգուրացիան JSON ձևաչափով.:

`pulumi config {{[-j|--json]}}`

- Դիտեք կոնֆիգուրացիան նշված կույտի համար.:

`pulumi config {{[-s|--stack]}} {{stack_name}}`

- Ստացեք կազմաձևման բանալի արժեքը.:

`pulumi config get {{key}}`

- Հեռացրեք կազմաձևման արժեքը.:

`pulumi config rm {{key}}`

- Սահմանեք արժեք ֆայլից կազմաձևման բանալիի համար.:

`cat {{path/to/file}} | pulumi config set {{key}}`

- Սահմանեք գաղտնի արժեք (օրինակ՝ API բանալի) կազմաձևման բանալիի համար և պահեք/ցուցադրեք որպես ծածկագրված տեքստ.:

`pulumi config set --secret {{key}} {{S3cr37_value}}`

- Հեռացրեք մի քանի կազմաձևման արժեքներ նշված կազմաձևման ֆայլից.:

`pulumi config --config-file {{path/to/file}} rm-all {{key1 key2 ...}}`
