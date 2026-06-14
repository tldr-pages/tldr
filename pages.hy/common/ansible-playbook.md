# ansible-playbook

> Կատարել առաջադրանքները, որոնք սահմանված են խաղատախտակի մեջ, հեռավոր մեքենաների վրա SSH-ի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://docs.ansible.com/projects/ansible/latest/cli/ansible-playbook.html>:.

- Գործարկել առաջադրանքները խաղային գրքում.:

`ansible-playbook {{playbook}}`

- Գործարկեք առաջադրանքները playbook-ում սովորական հյուրընկալող գույքագրմամբ.:

`ansible-playbook {{playbook}} {{[-i|--inventory]}} {{inventory_file}}`

- Գործարկեք առաջադրանքները playbook-ում հրամանի տողի միջոցով սահմանված լրացուցիչ փոփոխականներով.:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "{{variable1}}={{value1}} {{variable2}}={{value2}}"`

- Գործարկեք առաջադրանքները playbook-ում JSON ֆայլում սահմանված լրացուցիչ փոփոխականներով.:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "@{{variables.json}}"`

- Գործարկեք առաջադրանքները խաղային գրքում տվյալ պիտակների համար.:

`ansible-playbook {{playbook}} {{[-t|--tags]}} {{tag1,tag2}}`

- Գործարկեք առաջադրանքները խաղային գրքում՝ սկսած կոնկրետ առաջադրանքից.:

`ansible-playbook {{playbook}} --start-at {{task_name}}`

- Գործարկեք առաջադրանքները խաղային գրքում՝ առանց որևէ փոփոխության (չոր գործարկում).:

`ansible-playbook {{playbook}} {{[-C|--check]}} {{[-D|--diff]}}`
