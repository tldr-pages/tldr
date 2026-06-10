# pueue stash

> Պահպանեք առաջադրանքները, որպեսզի դրանք ինքնաբերաբար չսկսվեն:.
> Տես նաև՝ `pueue start`, `pueue enqueue`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Nukesor/pueue#how-to-use-it>:.

- Պահպանեք հերթագրված առաջադրանքը.:

`pueue stash {{task_id}}`

- Միանգամից պահեք բազմաթիվ առաջադրանքներ.:

`pueue stash {{task_id}} {{task_id}}`

- Անմիջապես սկսեք թաքցված առաջադրանքը.:

`pueue start {{task_id}}`

- Հերթագրեք առաջադրանքը, որը պետք է կատարվի, երբ նախորդ առաջադրանքները ավարտվեն.:

`pueue enqueue {{task_id}}`
