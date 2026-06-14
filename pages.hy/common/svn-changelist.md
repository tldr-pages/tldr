# svn փոփոխության ցուցակ

> Փոփոխությունների ցանկը կապեք մի շարք ֆայլերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn.c.changelist>:.

- Ավելացրեք ֆայլեր փոփոխության ցուցակին, ստեղծելով փոփոխության ցուցակը, եթե այն գոյություն չունի.:

`svn {{[cl|changelist]}} {{changelist_name}} {{path/to/file1 path/to/file2 ...}}`

- Հեռացրեք ֆայլերը փոփոխության ցուցակից.:

`svn {{[cl|changelist]}} --remove {{path/to/file1 path/to/file2 ...}}`

- Միանգամից հեռացնել ամբողջ փոփոխությունների ցանկը.:

`svn {{[cl|changelist]}} --remove {{[-R|--recursive]}} --changelist {{changelist_name}} .`

- Փոփոխությունների ցանկին ավելացրեք դիրեկտորիաների բացատով առանձնացված ցանկի բովանդակությունը.:

`svn {{[cl|changelist]}} {{[-R|--recursive]}} {{changelist_name}} {{path/to/directory1 path/to/directory2 ...}}`

- Կատարեք փոփոխության ցուցակ.:

`svn commit --changelist {{changelist_name}}`
