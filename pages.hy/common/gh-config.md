# gh կոնֆիգուրացիա

> Փոխել կոնֆիգուրացիան GitHub CLI-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_config>:.

- Ցուցադրել, թե ինչ Git արձանագրություն է օգտագործվում.:

`gh config get git_protocol`

- Սահմանել արձանագրությունը SSH:

`gh config set git_protocol ssh`

- Օգտագործեք `delta`-ը կողք կողքի ռեժիմում որպես լռելյայն փեյջեր բոլոր `gh` հրամանների համար.:

`gh config set pager 'delta --side-by-side'`

- Սահմանեք տեքստային խմբագրիչը Vim:

`gh config set editor {{vim}}`

- Վերականգնել լռելյայն տեքստային խմբագրին.:

`gh config set editor ""`

- Անջատել ինտերակտիվ հուշումները.:

`gh config set prompt {{disabled}}`

- Սահմանեք որոշակի կազմաձևման արժեք.:

`gh config set {{key}} {{value}}`
