#տեղադրել

> Պատճենել ֆայլերը և սահմանել ատրիբուտները:.
> Սովորաբար օգտագործվում է Makefiles-ի կողմից:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>:.

- Պատճենեք ֆայլերը նպատակակետին.:

`install {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Պատճենեք ֆայլերը դեպի նպատակակետ՝ սահմանելով դրանց սեփականությունը.:

`install {{[-o|--owner]}} {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Պատճենեք ֆայլերը դեպի նպատակակետ՝ սահմանելով դրանց խմբի սեփականությունը.:

`install {{[-g|--group]}} {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Պատճենեք ֆայլերը դեպի նպատակակետ՝ սահմանելով դրանց `mode`:

`install {{[-m|--mode]}} {{+x}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Պատճենեք ֆայլերը և կիրառեք աղբյուրի մուտքի/փոփոխման ժամանակները դեպի նպատակակետ.:

`install {{[-p|--preserve-timestamps]}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Պատճենեք ֆայլերը և ստեղծեք դիրեկտորիաներ նպատակակետում, եթե դրանք գոյություն չունեն.:

`install -D {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`
