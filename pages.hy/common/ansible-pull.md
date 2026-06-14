# ansible-pull

> Քաշեք անիմաստ գրքույկները VCS ռեպո-ից և գործարկեք դրանք տեղական հյուրընկալողի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.ansible.com/projects/ansible/latest/cli/ansible-pull.html>:.

- Քաշեք խաղագիրքը VCS-ից և գործարկեք լռելյայն `local.yml` խաղագիրք:

`ansible-pull {{[-U|--url]}} {{repository_url}}`

- Քաշեք խաղագիրք VCS-ից և գործարկեք հատուկ խաղագիրք.:

`ansible-pull {{[-U|--url]}} {{repository_url}} {{playbook}}`

- Քաշեք խաղագիրք VCS-ից որոշակի մասնաճյուղում և գործարկեք հատուկ խաղագիրք.:

`ansible-pull {{[-U|--url]}} {{repository_url}} {{[-C|--checkout]}} {{branch}} {{playbook}}`

- Քաշեք խաղագիրք VCS-ից, նշեք hosts ֆայլը և գործարկեք հատուկ խաղագիրք.:

`ansible-pull {{[-U|--url]}} {{repository_url}} {{[-i|--inventory]}} {{hosts_file}} {{playbook}}`
