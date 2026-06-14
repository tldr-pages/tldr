# xsv

> Rust-ով գրված CSV գործիքակազմ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/BurntSushi/xsv>:.

- Ստուգեք ֆայլի վերնագրերը.:

`xsv headers {{path/to/file.csv}}`

- Հաշվեք գրառումների քանակը.:

`xsv count {{path/to/file.csv}}`

- Ստացեք ակնարկ գրառումների ձևի մասին.:

`xsv stats {{path/to/file.csv}} | xsv table`

- Ընտրեք մի քանի սյունակներ.:

`xsv select {{column1,column2}} {{path/to/file.csv}}`

- Ցույց տալ 10 պատահական գրառում.:

`xsv sample {{10}} {{path/to/file.csv}}`

- Միացրեք սյունակը մեկ ֆայլից մյուսը.:

`xsv join --no-case {{column1}} {{path/to/file1.csv}} {{column2}} {{path/to/file2.csv}} | xsv table`
