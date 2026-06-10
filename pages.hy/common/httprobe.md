# http խալաթ

> Վերցրեք տիրույթների ցանկը և ստուգեք աշխատող HTTP և HTTPS սերվերների համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tomnomnom/httprobe>:.

- Հետազոտեք տիրույթների ցանկը տեքստային ֆայլից.:

`cat {{input_file}} | httprobe`

- Միայն ստուգեք HTTP-ի առկայությունը, եթե HTTPS-ը չի աշխատում.:

`cat {{input_file}} | httprobe --prefer-https`

- Հետազոտեք լրացուցիչ նավահանգիստները տվյալ արձանագրությամբ.:

`cat {{input_file}} | httprobe -p {{https:2222}}`

- Ցուցադրել օգնությունը.:

`httprobe --help`
