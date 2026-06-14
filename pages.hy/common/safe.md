#անվտանգ

> Շփվեք HashiCorp Vault-ի հետ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/egen/safe>:.

- Ավելացրեք անվտանգ թիրախ.:

`safe target {{vault_addr}} {{target_name}}`

- Նույնականացրեք CLI հաճախորդը Vault սերվերի դեմ՝ օգտագործելով վավերացման նշան.:

`safe auth {{authentication_token}}`

- Տպել միջավայրի փոփոխականները, որոնք նկարագրում են ընթացիկ թիրախը.:

`safe env`

- Ցուցադրել բոլոր հասանելի ստեղների ծառի հիերարխիան տվյալ ուղու համար.:

`safe tree {{path}}`

- Գաղտնիք տեղափոխեք մի ճանապարհից մյուսը.:

`safe move {{path/to/old_secret}} {{path/to/new_secret}}`

- Ստեղծեք նոր 2048-բիթանոց SSH բանալի-զույգ և պահեք այն.:

`safe ssh {{2048}} {{path/to/secret}}`

- Սահմանեք ոչ զգայուն ստեղներ գաղտնիքի համար.:

`safe set {{path/to/secret}} {{key}}={{value}}`

- Գաղտնի դրեք ավտոմատ ստեղծվող գաղտնաբառը.:

`safe gen {{path/to/secret}} {{key}}`
