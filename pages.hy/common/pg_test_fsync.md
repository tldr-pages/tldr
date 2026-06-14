# pg_test_fsync

> Որոշեք ձեր համակարգի ամենաարագ wal_sync_method-ը:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/pgtestfsync.html>:.

- Գործարկեք լռելյայն fsync հենանիշը (5 վայրկյան).:

`pg_test_fsync`

- Նշեք հատուկ փորձարկման տևողությունը.:

`pg_test_fsync {{[-s|--secs-per-test]}} {{seconds}}`

- Օգտագործեք հատուկ ֆայլի անուն (այն պետք է լինի նույն ֆայլային համակարգում, որտեղ գտնվում է կամ տեղադրվելու է pg_wal գրացուցակը).:

`pg_test_fsync {{[-f|--filename]}} {{path/to/file}}`
