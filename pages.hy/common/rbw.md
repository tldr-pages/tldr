# rbw

> Bitwarden-ի հետ համատեղելի գաղտնաբառերի ոչ պաշտոնական կառավարիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/doy/rbw#configuration>:.

- Մուտք գործեք պահոց.:

`rbw login`

- Բացեք պահոցը.:

`rbw unlock`

- Թվարկեք պահոցում գտնվող բոլոր իրերը.:

`rbw list`

- Ստացեք գաղտնաբառ մուտքի համար.:

`rbw get "{{entry_name}}"`

- Ստացեք օգտանուն մուտքի համար.:

`rbw get {{[-f|--field]}} username "{{entry_name}}"`

- Պատճենեք գաղտնաբառը clipboard-ում.:

`rbw get {{[-c|--clipboard]}} "{{entry_name}}"`

- Ստեղծեք նոր գաղտնաբառ նշված թվով նիշերով.:

`rbw generate {{password_length}}`

- Կողպեք պահոցը.:

`rbw lock`
