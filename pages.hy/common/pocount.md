# հաշիվ

> Translate Toolkit կոմունալ ֆայլից թարգմանության առաջընթաց ստանալու համար, որն աջակցում է մի քանի ձևաչափերի:.
> Լրացուցիչ տեղեկություններ. <https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pocount.html>:.

- Տպեք գունավոր աղյուսակ՝ ֆայլի թարգմանության առաջընթացով.:

`pocount {{path/to/file.po}}`

- Տպեք տարբեր ֆայլերի թարգմանության առաջընթացը, մեկ տող յուրաքանչյուր ֆայլի համար.:

`pocount --short {{translation_*.ts}}`

- Ստեղծեք CSV ֆայլ տարբեր ֆայլերի թարգմանության առաջընթացով.:

`pocount --csv {{translation_*.ts}} > {{path/to/translation_progress.csv}}`
