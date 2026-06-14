# նավակ

> Տեքստային տերմինալների RSS/Atom հոսքի ընթերցող:.
> Լրացուցիչ տեղեկություններ. <https://newsboat.org/releases/2.40/docs/newsboat.html#_first_steps>:.

- Առաջին ներմուծեք սնուցման URL-ները OPML ֆայլից.:

`newsboat {{[-i|--import-from-opml]}} {{my-feeds.xml}}`

- Այլընտրանք, ձեռքով ավելացրեք թարմացումներ.:

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- Սկսեք Newsboat-ը և թարմացրեք բոլոր թարմացումները գործարկման ժամանակ.:

`newsboat {{[-r|--refresh-on-start]}}`

- Կատարեք մեկ կամ մի քանի հրամաններ ոչ ինտերակտիվ ռեժիմով.:

`newsboat {{[-x|--execute]}} {{reload|print-unread|...}}`

- Տես ստեղնաշարի դյուրանցումները (առավել համապատասխանը տեսանելի է կարգավիճակի տողում).:

`<?>`
