# swc

> Rust-ով գրված JavaScript և TypeScript կոմպիլյատոր:.
> Լրացուցիչ տեղեկություններ. <https://swc.rs/docs/usage/cli>:.

- Տեղափոխեք նշված մուտքային ֆայլը և թողարկեք `stdout`:

`swc {{path/to/file}}`

- Տեղափոխեք մուտքագրված ֆայլը ամեն անգամ, երբ այն փոխվում է.:

`swc {{path/to/file}} {{[-w|--watch]}}`

- Փոխանցել նշված մուտքային ֆայլը և ելքը որոշակի ֆայլի.:

`swc {{path/to/input_file}} {{[-o|--out-file]}} {{path/to/output_file}}`

- Փոխանցել նշված մուտքագրման գրացուցակը և ելքը որոշակի գրացուցակ.:

`swc {{path/to/input_directory}} {{[-d|--out-dir]}} {{path/to/output_directory}}`

- Փոխանցել նշված մուտքագրման գրացուցակը, օգտագործելով հատուկ կազմաձևման ֆայլ.:

`swc {{path/to/input_directory}} --config-file {{path/to/.swcrc}}`

- Անտեսեք ֆայլերը գլոբալ ճանապարհի միջոցով նշված գրացուցակում.:

`swc {{path/to/input_directory}} --ignore {{path/to/ignored_file1 path/to/ignored_file2 ...}}`
