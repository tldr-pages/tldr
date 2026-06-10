# dolt կլոն

> Կլոնավորեք պահեստը նոր գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://docs.dolthub.com/cli-reference/cli#dolt-clone>:.

- Կլոնավորեք գոյություն ունեցող պահոցը որոշակի գրացուցակում (կանխադրված է պահեստի անունը).:

`dolt clone {{repository_url}} {{path/to/directory}}`

- Կլոնավորեք գոյություն ունեցող պահեստը և ավելացրեք հատուկ հեռակառավարիչ (կանխադրված է սկզբնաղբյուր).:

`dolt clone --remote {{remote_name}} {{repository_url}}`

- Կլոնավորեք գոյություն ունեցող պահոցը միայն որոշակի ճյուղ բերելով (կանխադրված բոլոր ճյուղերում).:

`dolt clone {{[-b|--branch]}} {{branch_name}} {{repository_url}}`

- Կլոնավորեք պահեստը, օգտագործելով AWS տարածաշրջանը (օգտագործում է պրոֆիլի լռելյայն շրջանը, եթե ոչ մեկը տրամադրված չէ).:

`dolt clone --aws-region {{region_name}} {{repository_url}}`

- Կլոնավորեք պահեստը, օգտագործելով AWS հավատարմագրերի ֆայլը.:

`dolt clone --aws-creds-file {{credentials_file}} {{repository_url}}`

- Կլոնավորեք պահոցը՝ օգտագործելով AWS հավատարմագրերի պրոֆիլը (օգտագործում է լռելյայն պրոֆիլը, եթե այն նախատեսված չէ).:

`dolt clone --aws-creds-profile {{profile_name}} {{repository_url}}`

- Կլոնավորեք պահեստը, օգտագործելով AWS հավատարմագրերի տեսակը.:

`dolt clone --aws-creds-type {{credentials_type}} {{repository_url}}`
