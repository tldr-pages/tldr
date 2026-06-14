# rpk

> Կառավարեք Redpanda-ի թեմաները, կլաստերները, խմբերը, անվտանգությունը և ավելին մեկ երկուականի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://docs.redpanda.com/current/reference/rpk/>:.

- Ստեղծեք նոր թեմա.:

`rpk topic create {{topic_name}}`

- Ստեղծեք հաղորդագրություն թեմայի վերաբերյալ.:

`rpk topic produce {{topic_name}}`

- Սպառեք բազմաթիվ թեմաներից հաղորդագրություններ.:

`rpk topic consume {{topic_name1 topic_name2 ...}}`

- Նշեք բոլոր թեմաները.:

`rpk topic list`

- Ցուցադրել կլաստերի տեղեկատվությունը.:

`rpk cluster info`

- Նշեք սպառողների բոլոր խմբերը.:

`rpk group list`

- Նկարագրեք սպառողների խումբը հետաձգման մասին տեղեկություններով.:

`rpk group describe {{group_name}}`

- Ցուցադրման տարբերակը:

`rpk version`
