# pyinfra

> Ավտոմատացնում է ենթակառուցվածքը մեծ մասշտաբով:.
> Լրացուցիչ տեղեկություններ. <https://docs.pyinfra.com/en/3.x/cli.html>:.

- Կատարեք հրաման SSH-ի վրա.:

`pyinfra {{target_ip_address}} exec -- {{command_name_and_arguments}}`

- Կատարել տեղակայման ֆայլի բովանդակությունը թիրախների ցանկում.:

`pyinfra {{path/to/target_list.py}} {{path/to/deploy.py}}`

- Կատարել հրամաններ տեղական.:

`pyinfra @local {{path/to/deploy.py}}`

- Կատարեք հրամաններ Docker-ի վրա.:

`pyinfra @docker/{{container}} {{path/to/deploy.py}}`
