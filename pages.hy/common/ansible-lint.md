# ansible-lint

> Կիրառեք կանոններ և հետևեք ձեր ավտոմատացման բովանդակության լավագույն փորձին:.
> Լրացուցիչ տեղեկություններ. <https://docs.ansible.com/projects/lint/>:.

- Տեղադրեք հատուկ խաղագիրք և դերերի գրացուցակ.:

`ansible-lint {{path/to/playbook_file}} {{path/to/role_directory}}`

- Փակեք խաղագիրքը՝ բացառելով հատուկ կանոնները.:

`ansible-lint {{[-x|--exclude-rules]}} {{rule1,rule2,...}} {{path/to/playbook_file}}`

- Տեղադրեք խաղագիրքը անցանց ռեժիմում և ձևաչափեք ելքը որպես PEP8:

`ansible-lint {{[-o|--offline]}} {{[-p|--parseable]}} {{path/to/playbook_file}}`

- Տեղադրեք խաղագիրք՝ օգտագործելով սովորական կանոնների գրացուցակը.:

`ansible-lint {{[-r|--rules]}} {{path/to/custom_rules_directory}} {{path/to/playbook_file}}`

- Ansible-ի ողջ բովանդակությունը ռեկուրսիվ կերպով տեղադրեք տվյալ գրացուցակում.:

`ansible-lint {{path/to/project_directory}}`
