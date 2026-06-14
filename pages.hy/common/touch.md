#հպում

> Ստեղծեք ֆայլեր և սահմանեք մուտքի/փոփոխման ժամանակները:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html>:.

- Ստեղծեք հատուկ ֆայլեր կամ թարմացրեք դրանց ժամանակացույցերը, եթե դրանք արդեն գոյություն ունեն.:

`touch {{path/to/file1 path/to/file2 ...}}`

- Սահմանեք ֆայլի [a]ccess կամ [m]փոփոխման ժամանակները ընթացիկին և մի ստեղծեք ֆայլ, եթե այն գոյություն չունի:

`touch {{[-c|--no-create]}} {{-a|-m}} {{path/to/file1 path/to/file2 ...}}`

- Սահմանեք ֆայլի [t] ժամանակը որոշակի արժեքի և մի ստեղծեք ֆայլ, եթե այն գոյություն չունի.:

`touch {{[-c|--no-create]}} -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- Ֆայլերի ժամանակի դրոշմը սահմանեք հղման ֆայլի ժամանակի դրոշմակնիքին և մի ստեղծեք ֆայլը, եթե այն գոյություն չունի.:

`touch {{[-c|--no-create]}} {{[-r|--reference]}} {{path/to/reference_file}} {{path/to/file1 path/to/file2 ...}}`

- Սահմանեք ժամանակի դրոշմը՝ վերլուծելով տողը.:

`touch {{[-d|--date]}} "{{last year|5 hours|next thursday|nov 14|...}}" {{path/to/file}}`

- Ստեղծեք բազմաթիվ ֆայլեր աճող թվով.:

`touch {{path/to/file{1..10}}}`

- Ստեղծեք բազմաթիվ ֆայլեր տառերի տիրույթով.:

`touch {{path/to/file{a..z}}}`
