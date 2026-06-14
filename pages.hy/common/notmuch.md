#ոչ շատ

> Ցուցադրեք, որոնեք, կարդացեք և նշեք էլփոստի հաղորդագրությունների մեծ հավաքածուները:.
> Լրացուցիչ տեղեկություններ. <https://notmuchmail.org/manpages/>:.

- Կարգավորել առաջին օգտագործման համար.:

`notmuch setup`

- Ավելացնել պիտակ բոլոր հաղորդագրությունների համար, որոնք համապատասխանում են որոնման տերմինին.:

`notmuch tag +{{custom_tag}} "{{search_term}}"`

- Հեռացրեք պիտակը որոնման տերմինին համապատասխանող բոլոր հաղորդագրությունների համար.:

`notmuch tag -{{custom_tag}} "{{search_term}}"`

- Հաշվեք տվյալ որոնման տերմինին համապատասխանող հաղորդագրությունները.:

`notmuch count --output={{messages|threads}} "{{search_term}}"`

- Որոնեք տվյալ որոնման տերմինին համապատասխանող հաղորդագրություններ.:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} "{{search_term}}"`

- Սահմանափակեք որոնման արդյունքների քանակը X-ով.:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} --limit={{X}} "{{search_term}}"`

- Ստեղծեք պատասխանի ձևանմուշ մի շարք հաղորդագրությունների համար.:

`notmuch reply --format={{default|headers-only}} --reply-to={{sender|all}} "{{search_term}}"`
