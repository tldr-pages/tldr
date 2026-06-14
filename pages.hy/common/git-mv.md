# git mv

> Տեղափոխեք կամ վերանվանեք ֆայլերը և թարմացրեք Git ինդեքսը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-mv>:.

- Տեղափոխեք ֆայլ ռեպո ներսում և ավելացրեք շարժումը հաջորդ հանձնառությանը.:

`git mv {{path/to/file}} {{path/to/destination}}`

- Վերանվանեք ֆայլը կամ գրացուցակը և ավելացրեք վերանվանումը հաջորդ commit-ին.:

`git mv {{path/to/file_or_directory}} {{path/to/destination}}`

- Վերագրանցեք ֆայլը կամ գրացուցակը նպատակային ուղու վրա, եթե այն գոյություն ունի.:

`git mv {{[-f|--force]}} {{path/to/file_or_directory}} {{path/to/destination}}`
