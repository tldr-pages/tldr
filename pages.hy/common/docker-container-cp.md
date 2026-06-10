# դոկեր կոնտեյներ cp

> Պատճենել ֆայլերը կամ գրացուցակները հյուրընկալող և բեռնարկղային ֆայլային համակարգերի միջև:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/container/cp/>:.

- Պատճենել ֆայլը կամ գրացուցակը հոսթից կոնտեյներ.:

`docker {{[cp|container cp]}} {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`

- Պատճենեք ֆայլը կամ գրացուցակը կոնտեյներից դեպի հյուրընկալող.:

`docker {{[cp|container cp]}} {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}`

- Պատճենեք ֆայլը կամ գրացուցակը հոսթից դեպի կոնտեյներ՝ հետևելով սիմհղումներին (ուղղակիորեն պատճենում է համակցված ֆայլերը, ոչ թե հենց սիմհղումները).:

`docker {{[cp|container cp]}} {{[-L|--follow-link]}} {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`
