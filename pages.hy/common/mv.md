# մվ

> Տեղափոխել կամ վերանվանել ֆայլերը և գրացուցակները:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>:.

- Վերանվանել ֆայլը կամ գրացուցակը, երբ թիրախը գոյություն ունեցող գրացուցակ չէ.:

`mv {{path/to/source}} {{path/to/target}}`

- Տեղափոխեք ֆայլը կամ գրացուցակը գոյություն ունեցող գրացուցակում.:

`mv {{path/to/source}} {{path/to/existing_directory}}`

- Տեղափոխեք բազմաթիվ ֆայլեր գոյություն ունեցող գրացուցակում՝ ֆայլերի անունները պահելով անփոփոխ.:

`mv {{path/to/source1 path/to/source2 ...}} {{path/to/existing_directory}}`

- Մի պահանջեք հաստատում առկա ֆայլերը վերագրելուց առաջ.:

`mv {{[-f|--force]}} {{path/to/source}} {{path/to/target}}`

- Գործող ֆայլերը վերագրելուց առաջ ինտերակտիվ կերպով հաստատման հուշում, անկախ ֆայլի թույլտվություններից.:

`mv {{[-i|--interactive]}} {{path/to/source}} {{path/to/target}}`

- Մի վերագրեք առկա ֆայլերը թիրախում.:

`mv {{[-n|--no-clobber]}} {{path/to/source}} {{path/to/target}}`

- Տեղափոխեք ֆայլերը մանրամասն ռեժիմով, ցույց տալով ֆայլերը դրանք տեղափոխելուց հետո.:

`mv {{[-v|--verbose]}} {{path/to/source}} {{path/to/target}}`

- Նշեք թիրախային գրացուցակը, որպեսզի կարողանաք օգտագործել արտաքին գործիքներ շարժական ֆայլեր հավաքելու համար.:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{path/to/target_directory}}`
