# hg կլոն

> Ստեղծեք գոյություն ունեցող պահեստի պատճենը նոր գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://www.mercurial-scm.org/help/commands/clone>:.

- Կլոնավորեք պահեստը նշված գրացուցակում.:

`hg clone {{remote_repository_source}} {{destination_path}}`

- Կլոնավորեք պահոցը կոնկրետ մասնաճյուղի ղեկավարի մոտ՝ անտեսելով հետագա պարտավորությունները.:

`hg clone {{[-b|--branch]}} {{branch}} {{remote_repository_source}}`

- Կլոնավորեք պահեստը միայն `.hg` գրացուցակով, առանց ֆայլերը ստուգելու.:

`hg clone {{[-U|--noupdate]}} {{remote_repository_source}}`

- Կլոնավորեք պահոցը կոնկրետ վերանայման, պիտակի կամ մասնաճյուղի վրա՝ պահպանելով ամբողջ պատմությունը.:

`hg clone {{[-u|--updaterev]}} {{revision}} {{remote_repository_source}}`

- Կլոնավորեք պահոցը մինչև որոշակի վերանայում առանց որևէ նոր պատմության.:

`hg clone {{[-r|--rev]}} {{revision}} {{remote_repository_source}}`
