#հասանելի

> Կառավարեք համակարգիչների խմբերը հեռակա կարգով SSH-ի միջոցով: (օգտագործեք `/etc/ansible/hosts` ֆայլը՝ նոր խմբեր/հոսթներ ավելացնելու համար):.
> Որոշ ենթահրամաններ, ինչպիսիք են `galaxy`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.ansible.com/projects/ansible/latest/cli/ansible.html>:.

- Ցուցակեք խմբին պատկանող հյուրընկալողներին.:

`ansible {{group}} --list-hosts`

- Ping մի խումբ հյուրընկալողներ՝ կանչելով ping մոդուլը.:

`ansible {{group}} {{[-m|--module-name]}} ping`

- Ցուցադրել փաստեր մի խումբ հոսթինգների մասին՝ կանչելով տեղադրման մոդուլը.:

`ansible {{group}} {{[-m|--module-name]}} setup`

- Կատարեք հրաման մի խումբ հոսթինգների վրա՝ կանչելով հրամանի մոդուլը փաստարկներով.:

`ansible {{group}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{my_command}}'`

- Կատարեք հրաման վարչական արտոնություններով.:

`ansible {{group}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{my_command}}'`

- Կատարեք հրաման՝ օգտագործելով անհատական գույքագրման ֆայլը.:

`ansible {{group}} {{[-i|--inventory]}} {{inventory_file}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{my_command}}'`

- Թվարկեք խմբերը գույքագրման մեջ.:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
