# օդաչու

> Շփվեք GitHub Copilot-ի հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli>:.

- Սկսեք ինտերակտիվ ռեժիմը.:

`copilot`

- Թույլատրել բոլոր ֆայլերի խմբագրումը.:

`copilot --allow-tool write`

- Վերսկսեք ամենավերջին նիստը.:

`copilot --continue`

- Վերսկսեք նախորդ նստաշրջանը՝ օգտագործելով նիստի ընտրիչը.:

`copilot --resume`

- Օգտագործեք հատուկ մոդել.:

`copilot --model "{{gpt-5}}"`

- Թույլատրել բոլոր Git հրամանները, բացի `git push`-ից:

`copilot --allow-tool 'shell(git:*)' --deny-tool 'shell(git push)'`

- Կատարեք հուշում անմիջապես առանց ինտերակտիվ ռեժիմի՝ միաժամանակ թույլ տալով `copilot`-ին գործարկել ցանկացած հրաման.:

`copilot {{[-p|--prompt]}} "{{Fix the bug in main.js}}" --allow-all-tools`
