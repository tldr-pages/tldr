# tarsnap

> Շահագործել հեռավոր Tarsnap կոդավորված կրկնօրինակները:.
> Նշում. Ձեզ հարկավոր չէ նշել բանալի ֆայլը և քեշի գրացուցակը, եթե դրանք կարգավորեք `/usr/local/etc/tarsnap.conf` կամ `~/.tarsnaprc`-ում:.
> Տես նաև՝ `tarsnap-keygen`:.
> Լրացուցիչ տեղեկություններ. <https://www.tarsnap.com/man-tarsnap.1.html>:.

- [c]ստեղծեք մեկ կամ մի քանի ֆայլերի կամ գրացուցակների պահուստային արխիվ՝ նշելով ծածկագրային բանալին և քեշի գրացուցակը.:

`tarsnap -c --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ցուցադրել, թե որքան տվյալներ կվերբեռնվեն.:

`tarsnap -c --dry-run --print-stats --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ցուցակ պահված արխիվները.:

`tarsnap --list-archives --keyfile {{path/to/key_file}}`

- [d]ջնջել կոնկրետ արխիվ.:

`tarsnap -d --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}}`

- Ցուցակ[t] կոնկրետ արխիվի բովանդակությունը [v]erbose ռեժիմում.:

`tarsnap -tv --keyfile {{path/to/key_file}} -f {{archive_name}}`

- Վերականգնել մեկ կամ մի քանի ֆայլ կամ գրացուցակ հատուկ արխիվից.:

`tarsnap -x --keyfile {{path/to/key_file}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Պատճենել արխիվը.:

`tarsnap -c --keyfile {{path/to/key_file}} -f {{new_archive_name}} @@{{source_archive_name}}`
