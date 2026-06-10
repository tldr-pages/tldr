# անսիբլ-գալակտիկա

> Կատարել Ansible Role-ի և Collection-ի հետ կապված տարբեր գործողություններ:.
> Լրացուցիչ տեղեկություններ. <https://docs.ansible.com/projects/ansible/latest/cli/ansible-galaxy.html>:.

- Ցուցակեք տեղադրված դերերը կամ հավաքածուները.:

`ansible-galaxy {{role|collection}} list`

- Փնտրեք դերի տարբեր մակարդակներով խոսակցական (`-v` պետք է նշվի վերջում):

`ansible-galaxy role search {{keyword}} -v{{vvvvv}}`

- Տեղադրել կամ հեռացնել դեր(ներ).:

`ansible-galaxy role {{install|remove}} {{role_name1 role_name2 ...}}`

- Ստեղծեք նոր դեր.:

`ansible-galaxy role init {{role_name}}`

- Ստացեք տեղեկատվություն դերի մասին.:

`ansible-galaxy role info {{role_name}}`

- Տեղադրել կամ հեռացնել հավաքածու(ներ).:

`ansible-galaxy collection {{install|remove}} {{collection_name1 collection_name2 ...}}`

- Ցուցադրել օգնություն դերերի կամ հավաքածուների վերաբերյալ.:

`ansible-galaxy {{role|collection}} {{[-h|--help]}}`
