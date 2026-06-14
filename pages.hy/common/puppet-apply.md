# տիկնիկային դիմում

> Կիրառել Տիկնիկային մանիֆեստները տեղական մակարդակում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/puppetlabs/puppet/blob/main/references/man/apply.md>:.

- Կիրառել մանիֆեստ.:

`puppet apply {{path/to/manifest}}`

- Կատարել տիկնիկային կոդը.:

`puppet apply --execute {{code}}`

- Օգտագործեք հատուկ մոդուլ և hiera կազմաձևման ֆայլ.:

`puppet apply --modulepath {{path/to/directory}} --hiera_config {{path/to/file}} {{path/to/manifest}}`
