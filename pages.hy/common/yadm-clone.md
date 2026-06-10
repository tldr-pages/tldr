# yadm կլոն

> Աշխատում է այնպես, ինչպես `git clone`: Բացի այդ, դուք կարող եք լրացուցիչ դրոշներ փոխանցել ձեր պահեստը կարգավորելու համար:.
> Եթե պահեստում կա bootstrap ֆայլ, ձեզ կառաջարկվի այն գործարկել:.
> Տես նաև՝ `git clone`:.
> Լրացուցիչ տեղեկություններ. <https://yadm.io/docs/common_commands>:.

- Կլոնավորեք գոյություն ունեցող պահեստը.:

`yadm clone {{remote_repository_location}}`

- Կլոնավորեք գոյություն ունեցող պահեստը, այնուհետև գործարկեք bootstrap ֆայլը.:

`yadm clone {{remote_repository_location}} --bootstrap`

- Կլոնավորեք գոյություն ունեցող պահեստը և կլոնավորելուց հետո մի գործարկեք bootstrap ֆայլը.:

`yadm clone {{remote_repository_location}} --no-bootstrap`

- Փոխեք աշխատանքային ծառը, որը yadm-ը կօգտագործի կլոնավորման ժամանակ.:

`yadm clone {{remote_repository_location}} --w {{worktree_file}}`

- Փոխեք մասնաճյուղը, որտեղից yadm-ը ֆայլեր է ստանում.:

`yadm clone {{remote_repository_location}} -b {{branch}}`

- Անտեսել առկա պահեստի տեղական մասնաճյուղը.:

`yadm clone {{remote_repository_location}} -f`
