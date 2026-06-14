# git force-clone

> Ստացեք `git clone`-ի հիմնական գործառույթը, բայց եթե նպատակակետ Git պահոցն արդեն գոյություն ունի, այն կստիպի վերակայել այն, որպեսզի նմանվի հեռակառավարման կլոնի:.
> `git-extras`-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tj/git-extras/blob/main/Commands.md#git-force-clone>:.

- Կլոնավորեք Git պահոցը նոր գրացուցակում.:

`git force-clone {{remote_repository_location}} {{path/to/directory}}`

- Կլոնավորեք Git պահոցը նոր գրացուցակի մեջ՝ ստուգելով որոշակի մասնաճյուղ.:

`git force-clone {{[-b|--branch]}} {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`

- Կլոնավորեք Git պահոցը Git պահոցի գոյություն ունեցող գրացուցակում՝ կատարելով ուժային վերականգնում՝ այն նմանեցնելով հեռակառավարմանը և ստուգելով որոշակի ճյուղ.:

`git force-clone {{[-b|--branch]}} {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`
