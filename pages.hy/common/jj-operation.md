# jj գործողություն

> Աշխատեք `jj` պահեստի գործառնական մատյանով:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation>:.

- Ցույց տալ գործողության մատյանը.:

`jj {{[op|operation]}} log`

- Հետարկել վերջին գործողությունը.:

`jj {{[op|operation]}} undo`

- Հետարկել տրված գործողությունը.:

`jj {{[op|operation]}} undo {{operation}}`

- Վերականգնել պահեստը իր վիճակին տվյալ գործողության ժամանակ.:

`jj {{[op|operation]}} restore {{operation}}`

- Ցուցադրել պահեստի փոփոխությունները գործողության մեջ.:

`jj {{[op|operation]}} show {{operation}}`

- Ցուցադրել գործողության փոփոխությունների վիճակագրությունը, ամփոփագիրը և հատվածը.:

`jj {{[op|operation]}} show {{--stat}} {{[-s|--summary]}} {{[-p|--patch]}} {{operation}}`
