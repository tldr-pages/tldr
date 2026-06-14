#հասկի

> Native Git կեռիկներն ավելի հեշտ են դարձել:.
> Լրացուցիչ տեղեկություններ. <https://typicode.github.io/husky/>:.

- Տեղադրեք Husky ընթացիկ գրացուցակում.:

`husky install`

- Տեղադրեք Husky-ը հատուկ գրացուցակում.:

`husky install {{path/to/directory}}`

- Սահմանեք հատուկ հրաման որպես `pre-push` կեռիկ Git-ի համար.:

`husky set {{.husky/pre-push}} "{{command}} {{command_arguments}}"`

- Ավելացրեք որոշակի հրաման ընթացիկ `pre-commit` կեռին.:

`husky add {{.husky/pre-commit}} "{{command}} {{command_arguments}}"`

- Տեղահանեք Husky կեռիկները ընթացիկ գրացուցակից.:

`husky uninstall`

- Ցուցադրել օգնությունը.:

`husky`
