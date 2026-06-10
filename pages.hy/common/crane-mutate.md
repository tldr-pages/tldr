# կռունկի մուտացիա

> Փոփոխել պատկերների պիտակները և ծանոթագրությունները:.
> Կոնտեյները պետք է տեղափոխվի գրանցամատյան, և մանիֆեստը թարմացվի այնտեղ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>:.

- Նոր ծանոթագրություններ սահմանելու համար (կանխադրված []):

`crane mutate {{[-a|--annotation]}}/{{[-l|--label]}} {{annotation/label}}`

- Պատկերին կցելու ուղի դեպի tarball/command/entrypoint/environment variable/exposed-ports:

`crane mutate {{--append}}/{{--cmd}}/{{--entrypoint}}/{{[-e|--env]}}/{{--exposed-ports}} {{var1 var2 ...}}`

- Ստացված պատկերի նոր թարբոլի ուղին.:

`crane mutate {{[-o|--output]}} {{path/to/tarball}}`

- Պահեստ `os/arch/variant:osversion,platform` ձևով՝ մուտացված պատկերը մղելու համար.:

`crane mutate --set-platform {{platform_name}}`

- Նոր պիտակի հղում՝ մուտացված պատկերին կիրառելու համար.:

`crane mutate {{[-t|--tag]}} {{tag_name}}`

- Նոր օգտվող սահմանելու համար.:

`crane mutate {{[-u|--user]}} {{username}}`

- Նոր աշխատանքային ռեժիսուրա՝ սահմանելու համար.:

`crane mutate {{[-w|--workdir]}} {{path/to/work_directory}}`

- Ցուցադրել օգնությունը.:

`crane mutate {{[-h|--help]}}`
