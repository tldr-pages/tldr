#թղթային բանալի

> OpenPGP բանալիների արխիվատոր:.
> Լրացուցիչ տեղեկություններ. <https://www.jabberwocky.com/software/paperkey/>:.

- Վերցրեք հատուկ գաղտնի բանալի և ստեղծեք տեքստային ֆայլ գաղտնի տվյալների հետ.:

`paperkey --secret-key {{path/to/secret_key.gpg}} --output {{path/to/secret_data.txt}}`

- Վերցրեք գաղտնի բանալի տվյալները `secret_data.txt`-ում և միացրեք այն հանրային բանալիի հետ՝ գաղտնի բանալին վերակառուցելու համար.:

`paperkey --pubring {{path/to/public_key.gpg}} --secrets {{path/to/secret_data.txt}} --output {{secret_key.gpg}}`

- Արտահանեք հատուկ գաղտնի բանալի և ստեղծեք տեքստային ֆայլ գաղտնի տվյալների հետ.:

`gpg --export-secret-key {{key}} | paperkey --output {{path/to/secret_data.txt}}`
