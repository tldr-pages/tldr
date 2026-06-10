# rclone

> Պատճենեք, համաժամացրեք կամ տեղափոխեք ֆայլեր և գրացուցակներ շատ ամպային ծառայություններից և դրանցից:.
> Լրացուցիչ տեղեկություններ. <https://rclone.org/commands/rclone/>:.

- Գործարկեք ինտերակտիվ ընտրացանկ՝ rclone-ը կարգավորելու համար.:

`rclone config`

- Ցուցակագրեք գրացուցակի բովանդակությունը rclone հեռակառավարման վրա.:

`rclone lsf {{remote_name}}:{{path/to/directory}}`

- Պատճենեք ֆայլը կամ գրացուցակը տեղական մեքենայից դեպի հեռավոր նպատակակետ.:

`rclone copy {{path/to/source_file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- Պատճենեք վերջին 24 ժամվա ընթացքում փոխված ֆայլերը տեղական մեքենայից հեռակառավարման վահանակում՝ խնդրելով օգտվողին հաստատել յուրաքանչյուր ֆայլ.:

`rclone copy {{[-i|--interactive]}} --max-age 24h {{remote_name}}:{{path/to/directory}} {{path/to/local_directory}}`

- Հայելապատել որոշակի ֆայլ կամ գրացուցակ (Նշում. ի տարբերություն պատճենի, համաժամեցումը հեռացնում է ֆայլերը հեռակառավարման վահանակից, եթե այն գոյություն չունի տեղում):

`rclone sync {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- Ջնջել հեռավոր ֆայլը կամ գրացուցակը (Նշում. `--dry-run` նշանակում է փորձարկում, հեռացնել այն իրականում ջնջելու հրամանից):

`rclone {{[-n|--dry-run]}} delete {{remote_name}}:{{path/to/file_or_directory}}`

- Mount rclone remote (փորձնական):

`rclone mount {{remote_name}}:{{path/to/directory}} {{path/to/mount_point}}`

- Ապամոնտաժեք rclone հեռակառավարման վահանակը, եթե `<Ctrl c>`-ը ձախողվի (փորձնական).:

`fusermount {{[-u|--update]}} {{path/to/mount_point}}`
