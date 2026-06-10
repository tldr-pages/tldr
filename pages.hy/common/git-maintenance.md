# git սպասարկում

> Գործարկել առաջադրանքները՝ օպտիմալացնելու Git պահեստի տվյալները:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-maintenance>:.

- Գրանցեք ընթացիկ պահոցը օգտագործողի պահեստների ցանկում, որպեսզի ամեն օր սպասարկվի.:

`git maintenance register`

- Պլանավորեք սպասարկման առաջադրանքները, որոնք կաշխատեն ընթացիկ պահոցում ամեն ժամ.:

`git maintenance start`

- Դադարեցրեք ընթացիկ պահեստի ֆոնային պահպանման ժամանակացույցը.:

`git maintenance stop`

- Հեռացրեք ընթացիկ պահոցը օգտագործողի սպասարկման պահոցների ցանկից.:

`git maintenance unregister`

- Ընթացիկ պահոցի վրա կատարեք հատուկ սպասարկման խնդիր.:

`git maintenance run --task {{commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch}}`
