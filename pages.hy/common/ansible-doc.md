# ansible-doc

> Ցուցադրել տեղեկատվություն Ansible գրադարաններում տեղադրված մոդուլների մասին:.
> Ցուցադրել պլագինների համառոտ ցանկը և դրանց կարճ նկարագրությունները:.
> Լրացուցիչ տեղեկություններ. <https://docs.ansible.com/projects/ansible/latest/cli/ansible-doc.html>:.

- Ցուցակեք գործողության հասանելի հավելվածները (մոդուլները).:

`ansible-doc {{[-l|--list]}}`

- Ցուցակե՛ք որոշակի տեսակի առկա պլագինները.:

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{[-l|--list]}}`

- Ցույց տալ տեղեկատվություն կոնկրետ գործողությունների հավելվածի (մոդուլի) մասին.:

`ansible-doc {{plugin_name}}`

- Ցույց տալ տեղեկատվություն հատուկ տեսակի հավելվածի մասին.:

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{plugin_name}}`

- Ցույց տալ խաղային գրքույկի հատվածը գործողությունների հավելվածի համար (մոդուլներ).:

`ansible-doc {{[-s|--snippet]}} {{plugin_name}}`

- Ցուցադրել գործողությունների հավելվածի (մոդուլի) մասին տեղեկությունները որպես JSON:

`ansible-doc {{[-j|--json]}} {{plugin_name}}`
