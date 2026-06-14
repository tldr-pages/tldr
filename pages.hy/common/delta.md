#դելտա

> Git և diff ելքի դիտիչ:.
> Տես նաև՝ `diff`, `difft`:.
> Լրացուցիչ տեղեկություններ. <https://dandavison.github.io/delta/full---help-output.html>:.

- Համեմատեք ֆայլերը կամ գրացուցակները.:

`delta {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Համեմատեք ֆայլերը կամ գրացուցակները՝ ցույց տալով տողերի համարները.:

`delta {{[-n|--line-numbers]}} {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Համեմատեք ֆայլերը կամ գրացուցակները՝ կողք կողքի ցույց տալով տարբերությունները.:

`delta {{[-s|--side-by-side]}} {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Համեմատեք ֆայլերը կամ գրացուցակները՝ անտեսելով Git-ի կազմաձևման ցանկացած կարգավորում.:

`delta --no-gitconfig {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Համեմատեք, ներկայացրեք commit հեշերը, ֆայլերի անունները և տողերի համարները որպես հիպերհղումներ՝ համաձայն տերմինալների էմուլյատորների հիպերհղման առանձնահատկությունների.:

`delta --hyperlinks {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Ցուցադրել ընթացիկ կարգավորումները.:

`delta --show-config`

- Ցուցադրել աջակցվող լեզուները և համապատասխան ֆայլերի ընդարձակումները.:

`delta --list-languages`
