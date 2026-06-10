# ժիրայի խնդիր

> Կառավարեք խնդիրները Jira նախագծում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ankitpokhrel/jira-cli#issue>:.

- Թվարկեք վերջին խնդիրները.:

`jira issue {{[ls|list]}}`

- Թվարկեք կոնկրետ օգտվողին հանձնարարված խնդիրները.:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} "{{email_or_display_name}}"`

- Թվարկե՛ք ինձ հանձնարարված բարձր առաջնահերթ խնդիրները.:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- Ստեղծեք խնդիր՝ օգտագործելով ինտերակտիվ հուշում.:

`jira issue create`

- Խմբագրել խնդիրը՝ օգտագործելով ինտերակտիվ հուշում.:

`jira issue edit`

- Օգտագործողին հանձնարարեք խնդրին՝ օգտագործելով ինտերակտիվ հուշում.:

`jira issue {{[asg|assign]}}`

- Տեղափոխեք խնդիրը որոշակի վիճակ.:

`jira issue {{[mv|move]}} {{issue_id}} "{{In Progress}}"`

- Բացեք խնդիրը տերմինալում՝ օգտագործելով `less`:

`jira issue view {{issue_id}}`
