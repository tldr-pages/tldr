# restiprofile ժամանակացույց

> Պահուստավորեք ժամանակացույցը և գործարկեք դրանք հետին պլանում:.
> Տես նաև՝ `restic`, `resticprofile`, `resticprofile-unschedule`:.
> Լրացուցիչ տեղեկություններ. <https://creativeprojects.github.io/resticprofile/schedules/configuration/index.html>:.

- Պլանավորեք լռելյայն պրոֆիլը.:

`resticprofile schedule`

- Պլանավորեք պրոֆիլը (կանխադրված պրոֆիլը «կանխադրված» է).:

`resticprofile --name "{{group_name}}" schedule`

- Պլանավորեք բոլոր պրոֆիլները.:

`resticprofile schedule --all`

- Մի սկսեք աշխատանքը տեղադրելուց հետո.:

`resticprofile schedule --no-start`

- Ցուցադրել պլանավորված աշխատանքների կարգավիճակը պրոֆիլի համար.:

`resticprofile status {{[-n|--name]}} {{profile_name}}`

- Գործարկել պլանավորված աշխատանքը ձեռքով (օգտագործվում է համակարգի ժամանակացույցի կողմից).:

`resticprofile run-schedule "backup@{{profile_name}}"`
