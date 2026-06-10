#ջրա ինձ

> Ցուցադրել կազմաձևված `jira` օգտվողին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ankitpokhrel/jira-cli#commands>:.

- Ցուցադրել կազմաձևված `jira` օգտվողը՝:

`jira me`

- Թվարկեք ինձ հանձնարարված խնդիրները.:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me)`

- Թվարկե՛ք ինձ հանձնարարված ընթացիկ սպրինտի խնդիրները.:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- Ցուցադրել օգնությունը.:

`jira me {{[-h|--help]}}`
