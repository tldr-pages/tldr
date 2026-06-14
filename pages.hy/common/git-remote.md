# git հեռակառավարման վահանակ

> Կառավարեք հետևված պահոցների հավաքածուն («հեռակառավարիչներ»):.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-remote>:.

- Թվարկեք առկա հեռակառավարման սարքերը իրենց անուններով և URL-ներով.:

`git remote {{[-v|--verbose]}}`

- Ցույց տալ տեղեկատվություն հեռակառավարման վահանակի մասին.:

`git remote show {{remote_name}}`

- Ավելացնել հեռակառավարման վահանակ.:

`git remote add {{remote_name}} {{remote_url}}`

- Փոխեք հեռակառավարման վահանակի URL-ը (օգտագործեք `--add` գոյություն ունեցող URL-ը պահելու համար).:

`git remote set-url {{remote_name}} {{new_url}}`

- Ցույց տալ հեռակառավարման վահանակի URL-ը.:

`git remote get-url {{remote_name}}`

- Հեռացնել հեռակառավարման վահանակը.:

`git remote remove {{remote_name}}`

- Վերանվանել հեռակառավարման վահանակը.:

`git remote rename {{old_name}} {{new_name}}`
