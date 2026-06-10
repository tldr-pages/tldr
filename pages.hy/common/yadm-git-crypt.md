# yadm git-crypt

> Git Crypt-ը հնարավորություն է տալիս թափանցիկ գաղտնագրել և վերծանել ֆայլերը Git պահոցում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/AGWA/git-crypt>:.

- Նախաձեռնեք ռեպո՝ Git Crypt-ն օգտագործելու համար.:

`yadm git-crypt init`

- Կիսեք պահոցը GPG-ի միջոցով.:

`yadm git-crypt add-gpg-user {{user_id}}`

- Կոդավորված ֆայլերով պահեստը կլոնավորելուց հետո բացեք դրանք.:

`yadm git-crypt unlock`

- Արտահանել սիմետրիկ գաղտնի բանալի.:

`yadm git-crypt export-key {{path/to/key_file}}`
