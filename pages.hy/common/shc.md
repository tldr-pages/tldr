#շկ

> Ընդհանուր կեղևի սցենարի կազմող:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/shc>:.

- Կազմել shell script:

`shc -f {{script}}`

- Կազմեք shell script և նշեք ելքային երկուական ֆայլ.:

`shc -f {{script}} -o {{binary}}`

- Կազմեք shell-ի սկրիպտ և սահմանեք գործարկվողի գործողության ժամկետը.:

`shc -f {{script}} -e {{dd/mm/yyyy}}`

- Կազմեք shell script և սահմանեք հաղորդագրություն, որը կցուցադրվի ժամկետի ավարտից հետո.:

`shc -f {{script}} -e {{dd/mm/yyyy}} -m "{{Please contact your provider}}"`
