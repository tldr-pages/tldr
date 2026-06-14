# ստանալտեքստ

> Թարգմանում է տող՝ օգտագործելով պահված թարգմանությունները կազմված `.mo` ֆայլում:.
> Թարգմանությունները պահվում են `/usr/share/locale/locale_name/LC_MESSAGES/`-ում, որտեղ `domain` ֆայլի անվանումն է՝ առանց դրա ընդլայնման:.
> Տես նաև՝ `msgfmt`, `msgunfmt`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/gettext/manual/gettext.html#gettext-Invocation>:.

- Ստացեք տողի թարգմանությունը, ինչպես նշված է տիրույթի ֆայլում (վերադառնում է նշված `msgid`-ին, եթե թարգմանություն չկա):

`LANGUAGE={{locale}} gettext {{[-d|--domain]}} {{domain}} "{{msgid}}"`

- Ցուցադրել օգնությունը.:

`gettext {{[-h|--help]}}`

- Ցուցադրման տարբերակը:

`gettext {{[-V|--version]}}`
