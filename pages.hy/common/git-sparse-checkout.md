# git sparse-checkout

> Ստուգեք պահեստի ֆայլերի միայն մի մասը՝ ամեն ինչ կլոնավորելու կամ ստուգելու փոխարեն:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/git-sparse-checkout>:.

- Միացնել նոսր վճարումը.:

`git sparse-checkout init`

- Անջատեք նոսր վճարումը և վերականգնեք ամբողջական պահեստը.:

`git sparse-checkout disable`

- Նշեք, թե որ գրացուցակները (կամ ֆայլերը) ներառել.:

`git sparse-checkout set {{path/to/directory}}`

- Ավելի ուշ ավելացրեք ավելի շատ ուղիներ.:

`git sparse-checkout add {{path/to/directory}}`
