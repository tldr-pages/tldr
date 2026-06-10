# jira sprint

> Կառավարեք սպրինտները Jira նախագծի տախտակում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ankitpokhrel/jira-cli#sprint>:.

- Թվարկեք սպրինտները և դրանց խնդիրները հետազոտողի տեսքով.:

`jira sprint {{[ls|list]}}`

- Թվարկեք ընթացիկ սպրինտի խնդիրները.:

`jira sprint {{[ls|list]}} --current`

- Թվարկե՛ք ինձ հանձնարարված ընթացիկ սպրինտի խնդիրները.:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- Թվարկե՛ք ինձ հանձնարարված ընթացիկ սպրինտի բարձր առաջնահերթ խնդիրները.:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- Խնդիրներ ավելացրեք սպրինտին, օգտագործելով ինտերակտիվ հուշում.:

`jira sprint add`
