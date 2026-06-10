# sfdk կազմաձև

> Կարգավորել sfdk-ը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/10-general/doc/command.config.adoc>:.

- Ցուցադրել կոնֆիգուրացիան բոլոր շրջանակներով.:

`sfdk config --show`

- Սահմանեք կազմաձևման արժեքը.:

`sfdk config {{name}}={{value}}`

- Քողարկել տարբերակը որպես դատարկ.:

`sfdk config {{name}}=`

- Քողեք տարբերակը որպես դատարկ՝ առանց այն մղելու ներքին շրջանակում.:

`sfdk config {{name}}`

- Մաքրել ընտրանքի արժեքը.:

`sfdk --drop {{name}}`

- Գործարկեք ենթահրամանը նշված շրջանակում (`global`, `session` կամ `command`):

`sfdk config --{{scope}} {{subcommand}}`
