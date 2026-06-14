# git յուրաքանչյուրի համար

> Ցուցակեք և ընտրովի ձևաչափեք հղումները (ճյուղեր, պիտակներ) Git պահեստում:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-for-each-ref>:.

- Թվարկեք բոլոր ռեֆերատները (ճյուղեր և պիտակներ).:

`git for-each-ref`

- Նշեք միայն մասնաճյուղերը.:

`git for-each-ref refs/heads/`

- Նշեք միայն պիտակները.:

`git for-each-ref refs/tags/`

- Ցուցադրել `HEAD`-ում միավորված մասնաճյուղերը՝:

`git for-each-ref --merged HEAD refs/heads/`

- Թվարկեք բոլոր պատասխանողների կարճ անունները.:

`git for-each-ref --format "%(refname:short)"`

- Տեսակավորել ռեֆերատները ըստ կատարողի ամսաթվի (առաջինը ամենավերջին).:

`git for-each-ref --sort -committerdate`

- Տեսակավորել ռեֆերատները ըստ կատարողի ամսաթվի (առաջին հերթին ամենահինը).:

`git for-each-ref --sort committerdate`

- Սահմանափակեք արդյունքը որոշակի թվով refs-ներով.:

`git for-each-ref --count {{count}}`
