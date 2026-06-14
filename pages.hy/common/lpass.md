# lpass

> Ինտերֆեյս LastPass գաղտնաբառերի կառավարչի համար:.
> Լրացուցիչ տեղեկություններ. <https://lastpass.github.io/lastpass-cli/lpass.1.html>:.

- Մուտք գործեք ձեր LastPass հաշիվ՝ մուտքագրելով ձեր հիմնական գաղտնաբառը, երբ հուշում է.:

`lpass login {{username}}`

- Ցույց տալ մուտքի կարգավիճակը.:

`lpass status`

- Թվարկեք բոլոր կայքերը խմբավորված ըստ կատեգորիաների.:

`lpass ls`

- Ստեղծեք նոր գաղտնաբառ gmail.com-ի համար `myinbox` նույնացուցիչով և ավելացրեք LastPass-ին.:

`lpass generate --username {{username}} --url {{gmail.com}} {{myinbox}} {{password_length}}`

- Ցույց տալ գաղտնաբառը նշված մուտքի համար.:

`lpass show {{myinbox}} --password`
