# az մատակարար

> Կառավարեք ռեսուրսների մատակարարներին:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/provider>:.

- Գրանցեք մատակարար.:

`az provider register {{[-n|--namespace]}} {{Microsoft.PolicyInsights}}`

- Ապագրանցել մատակարարին.:

`az provider unregister {{[-n|--namespace]}} {{Microsoft.Automation}}`

- Նշեք բոլոր մատակարարներին բաժանորդագրության համար.:

`az provider list`

- Ցույց տալ տեղեկատվություն կոնկրետ մատակարարի մասին.:

`az provider show {{[-n|--namespace]}} {{Microsoft.Storage}}`

- Նշեք ռեսուրսների բոլոր տեսակները կոնկրետ մատակարարի համար.:

`az provider list --query "[?namespace=='{{Microsoft.Network}}'].resourceTypes[].resourceType"`
