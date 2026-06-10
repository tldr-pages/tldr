# gh գործակալ-առաջադրանք

> Կառավարեք GitHub գործակալի առաջադրանքները:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_agent-task>:.

- Թվարկեք գործակալի ամենավերջին առաջադրանքները.:

`gh {{[agent|agent-task]}} list`

- Ստեղծեք նոր գործակալի առաջադրանք ընթացիկ պահեստի համար.:

`gh {{[agent|agent-task]}} create "{{Improve the performance of the data processing pipeline}}"`

- Ստեղծեք նոր գործակալի առաջադրանք ֆայլից.:

`gh {{[agent|agent-task]}} create {{[-F|--from-file]}} {{path/to/file}}`

- Դիտեք մանրամասներ կոնկրետ գործակալի առաջադրանքի վերաբերյալ.:

`gh {{[agent|agent-task]}} view {{session_id|pr_number|url|branch}}`

- Ցույց տալ որոշակի գործակալի առաջադրանքի գրանցամատյանը.:

`gh {{[agent|agent-task]}} view --log {{session_id|pr_number|url|branch}}`
