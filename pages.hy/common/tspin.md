# ճ/գ

> Մատյան ֆայլի ընդգծող՝ հիմնված `less` փեյջերի վրա և հիմնականում իրեն պահում է ինչպես ցանկացած փեյջեր:.
> Լրացուցիչ տեղեկություններ. <https://github.com/bensadeh/tailspin#usage>:.

- Դիտեք գրանցամատյանի ֆայլը՝ օգտագործելով լռելյայն փեյջերը (`less`):

`tspin {{path/to/file.log}}`

- Կարդացեք մեկ այլ հրամանից և տպեք `stdout`:

`{{command}} | tspin`

- Կարդացեք ֆայլից և տպեք `stdout`՝ առանց էջավորման.:

`tspin {{path/to/file.log}} {{[-p|--print]}}`

- Հետևեք ֆայլին (նմանում է `tail -f`) և ընդգծեք նոր գրառումները.:

`tspin {{[-f|--follow]}} {{path/to/file.log}}`

- Նշեք միայն որոշակի խմբեր (հնարավոր արժեքներ՝ `numbers`, `urls`, `pointers`, `dates`, `paths`, `quotes`, `urls`, `pointers`, `paths`, `quotes`, __INLINE_CODE_CO, `ip-addresses`, `processes`, `json`):

`tspin --enable {{urls,ip-addresses,...}} {{path/to/file.log}}`

- Օգտագործեք հատուկ փեյջեր (`[FILE]` տողը պարտադիր բառացի տեղապահ է).:

`tspin --pager "{{bat -p}} [FILE]" {{path/to/file.log}}`

- Ընդգծեք սովորական տողերը հատուկ գույներով.:

`tspin --highlight {{red}}:{{ERROR,WARNING,...}} {{path/to/file.log}}`

- Գործարկեք տրված հրամանը և դիտեք ելքը `less`-ում:

`tspin --exec='{{command}}'`
