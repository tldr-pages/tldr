# rvm

> Հեշտությամբ տեղադրեք, կառավարեք և աշխատեք մի քանի ruby միջավայրերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://rvm.io/rvm/cli>:.

- Տեղադրեք Ruby-ի մեկ կամ մի քանի տարբերակներ.:

`rvm install {{version1 version2 ...}}`

- Ցուցադրել տեղադրված տարբերակների ցանկը.:

`rvm list`

- Օգտագործեք Ruby-ի հատուկ տարբերակը.:

`rvm use {{version}}`

- Սահմանեք Ruby-ի լռելյայն տարբերակը.:

`rvm --default use {{version}}`

- Թարմացրեք Ruby-ի տարբերակը նոր տարբերակի.:

`rvm upgrade {{current_version}} {{new_version}}`

- Տեղահանեք Ruby-ի տարբերակը և պահեք դրա աղբյուրները.:

`rvm uninstall {{version}}`

- Հեռացրեք Ruby-ի տարբերակը և դրա աղբյուրները.:

`rvm remove {{version}}`

- Ցույց տվեք ձեր OS-ի հատուկ կախվածությունները.:

`rvm requirements`
