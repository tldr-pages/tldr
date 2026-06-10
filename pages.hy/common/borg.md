#բորգ

> Կրկնօրինակման գործիքի կրկնօրինակում:.
> Ստեղծեք տեղական կամ հեռավոր կրկնօրինակներ, որոնք կարող են տեղադրվել որպես ֆայլային համակարգեր:.
> Լրացուցիչ տեղեկություններ. <https://borgbackup.readthedocs.io/en/stable/usage/general.html>:.

- Նախաձեռնել (տեղական) պահեստ.:

`borg init {{path/to/repo_directory}}`

- Կրկնօրինակեք գրացուցակը պահեստում՝ ստեղծելով արխիվ, որը կոչվում է «Երկուշաբթի».:

`borg create --progress {{path/to/repo_directory}}::{{Monday}} {{path/to/source_directory}}`

- Թվարկեք բոլոր արխիվները պահեստում.:

`borg list {{path/to/repo_directory}}`

- Հեռավոր պահոցում հանեք որոշակի գրացուցակ «Երկուշաբթի» արխիվից՝ բացառելով բոլոր `*.ext` ֆայլերը.:

`borg extract {{user}}@{{host}}:{{path/to/repo_directory}}::{{Monday}} {{path/to/target_directory}} --exclude '{{*.ext}}'`

- Կտրեք շտեմարանը՝ ջնջելով 7 օրից ավելի հին արխիվները՝ թվարկելով փոփոխությունները.:

`borg prune --keep-within {{7d}} --list {{path/to/repo_directory}}`

- Տեղադրեք պահեստը որպես FUSE ֆայլային համակարգ.:

`borg mount {{path/to/repo_directory}}::{{Monday}} {{path/to/mountpoint}}`

- Ցուցադրել օգնություն արխիվների ստեղծման վերաբերյալ.:

`borg create --help`
