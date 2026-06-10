# gdm

> GNOME Display Manager-ը (GDM) փոխարինում է X Display Manager-ին (XDM):.
> Տես նաև՝ `gdm-binary`, `gdmsetup`, `gdm-stop`, `gdm-restart`, `gdm-safe-restart`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/gdm>:.

- Գործարկեք GNOME Display Manager հավելվածը.:

`gdm`

- Կանխարգելել `gdm`-ի գործարկումը որպես դեյմոն ֆոնային գործընթաց.:

`gdm --nodaemon`

- Անջատեք `gdm` կառավարումը տեղական կոնսոլի X սերվերների համար առանց գլխի կամ հեռավոր միջավայրերի.:

`gdm --no-console`

- Կանխել շրջակա միջավայրի ախտահանման փոփոխականները, որոնք սկսվում են `$LD_`-ով.:

`gdm --preserve-ld-vars`

- Ցուցադրել օգնությունը.:

`gdm --help`

- Ցուցադրման տարբերակը:

`gdm --version`
