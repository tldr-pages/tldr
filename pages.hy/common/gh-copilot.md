# gh օդաչու

> Շփվեք GitHub Copilot-ի հետ:.
> Նշում. հնացած է `copilot`-ի օգտին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/github/gh-copilot#usage>:.

- Առաջարկեք հրաման՝ տրված նկարագրությամբ.:

`gh copilot suggest "{{Install git}}"`

- Առաջարկեք Git հրաման.:

`gh copilot suggest {{[-t|--target]}} git "{{Undo the most recent local commits}}"`

- Բացատրեք հրաման.:

`gh copilot explain "{{traceroute example.com}}"`

- Ստեղծեք Bash-ի համար նախատեսված կեղևի հատուկ անուններ.:

`echo 'eval "$(gh copilot alias -- bash)"' >> ~/.bashrc`

- Ստեղծեք կեղևի հատուկ անունները Zsh-ի համար:

`echo 'eval "$(gh copilot alias -- zsh)"' >> ~/.zshrc`

- Կարգավորել ընտրանքները.:

`gh copilot config`
