# keepassxc-cli

> Ինտերֆեյս KeePassXC-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/keepassxc-cli>:.

- Որոնման գրառումներ.:

`keepassxc-cli search {{path/to/database_file}} {{name}}`

- Թվարկեք թղթապանակի բովանդակությունը.:

`keepassxc-cli ls {{path/to/database_file}} {{path/to/directory}}`

- Ավելացրեք մուտքագրում ավտոմատ ստեղծված գաղտնաբառով.:

`keepassxc-cli add {{[-g|--generate]}} {{path/to/database_file}} {{entry_name}}`

- Ջնջել գրառումը.:

`keepassxc-cli rm {{path/to/database_file}} {{entry_name}}`

- Պատճենեք մուտքի գաղտնաբառը clipboard-ում.:

`keepassxc-cli clip {{path/to/database_file}} {{entry_name}}`

- Պատճենեք TOTP կոդը clipboard-ում.:

`keepassxc-cli clip {{[-t|--totp]}} {{path/to/database_file}} {{entry_name}}`

- Ստեղծեք անցաբառ 7 բառով.:

`keepassxc-cli diceware {{[-W|--words]}} 7`

- Ստեղծեք գաղտնաբառ 16 տպվող ASCII նիշերով.:

`keepassxc-cli generate {{[-lUns|--lower --upper --numeric --special]}} {{[-L|--length]}} 16`
