# gh քեշ

> Կառավարեք GitHub Actions քեշերը:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_cache>:.

- Ցուցակեք պահոցները ընթացիկ պահոցի համար.:

`gh cache {{[ls|list]}}`

- Ցուցակեք պահոցները կոնկրետ պահոցի համար.:

`gh cache {{[ls|list]}} {{[-R|--repo]}} {{owner}}/{{repository}}`

- Ցուցակեք քեշերը հատուկ քեշի հիմնական նախածանցով.:

`gh cache {{[ls|list]}} {{[-k|--key]}} {{key_prefix}}`

- Նշեք քեշերը որոշակի ճյուղի համար.:

`gh cache {{[ls|list]}} {{[-r|--ref]}} refs/heads/{{branch_name}}`

- Ցուցակեք քեշերը՝ տեսակավորված ըստ ամենաքիչ վերջերս հասանելիության՝:

`gh cache {{[ls|list]}} {{[-S|--sort]}} last_accessed_at {{[-O|--order]}} asc`

- Ջնջել քեշը ID-ով.:

`gh cache delete {{cache_id}}`

- Ջնջել քեշը բանալիով.:

`gh cache delete {{cache_key}}`

- Ջնջել բոլոր քեշերը.:

`gh cache delete {{[-a|--all]}}`
