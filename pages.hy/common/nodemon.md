# nodemon

> Դիտեք ֆայլերը և ավտոմատ կերպով վերագործարկեք հանգույցի հավելվածը, երբ փոփոխություններ հայտնաբերվեն:.
> Լրացուցիչ տեղեկություններ. <https://github.com/remy/nodemon/tree/main/doc/cli>:.

- Կատարեք նշված ֆայլը և դիտեք որոշակի ֆայլ փոփոխությունների համար.:

`nodemon {{path/to/file.js}}`

- Ձեռքով վերագործարկեք nodemon-ը (նշման nodemon-ը պետք է արդեն ակտիվ լինի, որպեսզի այն աշխատի).:

`rs`

- Անտեսեք հատուկ ֆայլեր.:

`nodemon {{[-i|--ignore]}} {{path/to/file_or_directory}}`

- Փաստարկներ փոխանցեք հանգույցի հավելվածին.:

`nodemon {{path/to/file.js}} {{arguments}}`

- Փոխանցեք արգումենտներն ինքնին հանգույցին, եթե դրանք արդեն նոդեմոն արգումենտներ չեն (օրինակ՝ `--inspect`):

`nodemon {{arguments}} {{path/to/file.js}}`

- Գործարկել կամայական ոչ հանգույցի սցենար.:

`nodemon {{[-x|--exec]}} "{{command_to_run_script}} {{options}}" {{path/to/script}}`

- Գործարկել Python սցենար.:

`nodemon {{[-x|--exec]}} "python {{options}}" {{path/to/file.py}}`
