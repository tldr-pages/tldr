# pg_combinebackup

> Վերակառուցեք ամբողջական (սինթետիկ) PostgreSQL կրկնօրինակը լրացուցիչ պահեստային շղթայից:.
> Բազմաթիվ կրկնօրինակներ նշելիս պատվիրեք դրանք ամենահինից մինչև նորագույնը:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgcombinebackup.html>:.

- Միավորել ամբողջական և աստիճանական կրկնօրինակը մեկ սինթետիկ ամբողջական կրկնօրինակում.:

`pg_combinebackup {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}}`

- Կատարեք չոր վազք՝ ցույց տալու համար, թե ինչ է արվելու՝ առանց ֆայլեր ստեղծելու.:

`pg_combinebackup {{[-n|--dry-run]}} {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}}`

- Ֆայլերը պատճենելու փոխարեն օգտագործեք կոշտ հղումներ (ավելի արագ, պահանջվում է նույն ֆայլային համակարգը).:

`pg_combinebackup {{[-k|--link]}} {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}}`

- Օգտագործեք ֆայլերի կլոնավորում (վերահղումներ) արդյունավետ պատճենման համար, եթե աջակցվում է.:

`pg_combinebackup --clone {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}}`

- Արդյունավետ պատճենման համար օգտագործեք `copy_file_range` համակարգի զանգը՝:

`pg_combinebackup --copy-file-range {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}}`

- Վերակառուցման ընթացքում սեղանի տարածքի տեղափոխում.:

`pg_combinebackup {{path/to/backup1 path/to/backup2 ...}} {{[-T|--tablespace-mapping]}} /{{path/to/old_tablespace}}=/{{path/to/new_tablespace}} {{[-o|--output]}} {{path/to/output_directory}}`

- Անջատեք fsync-ը ավելի արագ, բայց ոչ անվտանգ գրելու համար (միայն թեստավորում).:

`pg_combinebackup {{[-N|--no-sync]}} {{path/to/backup1 path/to/backup2 ...}} {{[-o|--output]}} {{path/to/output_directory}}`

- Ցույց տալ վրիպազերծման մանրամասն ելքը.:

`pg_combinebackup {{[-d|--debug]}} {{path/to/backup1 path/to/backup2 ...}} {{[-o|--output]}} {{path/to/output_directory}}`
