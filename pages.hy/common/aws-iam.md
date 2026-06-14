# aws ես

> Փոխազդել ինքնության և մուտքի կառավարման (IAM) հետ՝ վեբ ծառայություն՝ AWS ծառայությունների հասանելիությունը անվտանգ վերահսկելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/iam/>:.

- Ցանկ օգտագործողներին.:

`aws iam list-users`

- Ցանկի քաղաքականություն.:

`aws iam list-policies`

- Ցանկ խմբեր.:

`aws iam list-groups`

- Ստացեք օգտվողներին խմբում.:

`aws iam get-group --group-name {{group_name}}`

- Նկարագրեք IAM-ի քաղաքականությունը.:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{policy_name}}`

- Ցուցակ մուտքի ստեղներ.:

`aws iam list-access-keys`

- Ցուցակ մուտքի ստեղները կոնկրետ օգտագործողի համար.:

`aws iam list-access-keys --user-name {{user_name}}`

- Ցուցադրել օգնությունը.:

`aws iam help`
