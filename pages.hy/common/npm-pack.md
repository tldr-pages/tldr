# npm փաթեթ

> Ստեղծեք tarball փաթեթից:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/pack/>:.

- Ստեղծեք tarball ընթացիկ փաթեթից ընթացիկ գրացուցակում.:

`npm pack`

- Ստեղծեք tarball որոշակի փաթեթի թղթապանակից.:

`npm pack {{path/to/package_directory}}`

- Կատարեք չոր վազք՝ նախադիտելու tarball բովանդակությունը՝ առանց այն ստեղծելու.:

`npm pack --dry-run`

- Ստեղծեք tarball առանց կյանքի ցիկլի սցենարներ գործարկելու.:

`npm pack --ignore-scripts`

- Նշեք հատուկ ռեեստր՝ փաթեթի մետատվյալները ստանալու համար՝:

`npm pack --registry {{https://registry.npmjs.org/}}`
