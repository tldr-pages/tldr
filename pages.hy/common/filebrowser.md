# ֆայլի զննարկիչ

> Պարզ HTTP վեբ սերվեր՝ ֆայլերը և գրացուցակները կառավարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://filebrowser.org/cli/filebrowser.html>:.

- Սկսեք նոր սերվերի օրինակ, որը սպասարկում է ընթացիկ գրացուցակը.:

`filebrowser`

- Սկսեք նոր սերվերի օրինակ, որը սպասարկում է որոշակի արմատային գրացուցակ.:

`filebrowser {{[-r|--root]}} {{path/to/directory}}`

- Սկսեք օրինակ՝ տարբեր հյուրընկալող հասցեով (կանխադրված՝ `127.0.0.1`) և միացք (կանխադրված՝ `8080`):

`filebrowser {{[-a|--address]}} {{host}} {{[-p|--port]}} {{port}} {{[-r|--root]}} {{path/to/directory}}`

- Սկսեք օրինակը նշված կազմաձևման ֆայլով, որը պահում է հավելվածի տվյալների բազան որոշակի վայրում (կանխադրված է `filebrowser.db` ընթացիկ գրացուցակում):

`filebrowser {{[-c|--config]}} {{path/to/file}} {{[-d|--database]}} {{path/to/database.db}} {{[-r|--root]}} {{path/to/directory}}`

- Նախադրեք այլ կանխադրված առաջին անգամ հաշվի օգտանուն և գաղտնաբառ (երկուսն էլ կանխադրված են `admin`), երբ ստեղծեք նոր օրինակ.:

`filebrowser --username {{username}} --password {{password}} {{[-r|--root]}} {{path/to/directory}}`

- Սահմանեք պատկերի պրոցեսորների առավելագույն քանակը, որոնք օգտագործվում են մանրապատկերներ ստեղծելիս (կանխադրված է `4`):

`filebrowser --img-processors {{4}} {{[-r|--root]}} {{path/to/directory}}`

- Անջատեք պատկերների մանրապատկերները, ինչպես նաև «Command Runner» ֆունկցիան՝ սահմանափակելով մուտքը հոսթագրված սցենարի ֆայլերի՝ հավելվածի ներսում գործարկվելուց.:

`filebrowser --disable-exec --disable-thumbnails {{[-r|--root]}} {{path/to/directory}}`

- Անջատել պատկերների նախադիտումների չափափոխումը, ինչպես նաև հայտնաբերել ֆայլերի տեսակները՝ կարդալով դրանց վերնագրերը.:

`filebrowser --disable-preview-resize --disable-type-detection-by-header {{[-r|--root]}} {{path/to/directory}}`
