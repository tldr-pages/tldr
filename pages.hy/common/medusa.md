#մեդուզա

> Մոդուլային և զուգահեռ մուտքի բիրտ ուժային միջոց մի շարք արձանագրությունների համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/medusa>:.

- Նշեք բոլոր տեղադրված մոդուլները.:

`medusa -d`

- Ցույց տվեք կոնկրետ մոդուլի օգտագործման օրինակ (օգտագործեք `medusa -d` բոլոր տեղադրված մոդուլները ցուցակագրելու համար).:

`medusa -M {{ssh|http|web-form|postgres|ftp|mysql|...}} -q`

- Կիրառեք կոպիտ ուժ FTP սերվերի նկատմամբ՝ օգտագործելով օգտվողի անուններ պարունակող ֆայլ և գաղտնաբառեր պարունակող ֆայլ.:

`medusa -M ftp -h host -U {{path/to/username_file}} -P {{path/to/password_file}}`

- Կատարեք մուտքի փորձ HTTP սերվերի դեմ՝ օգտագործելով նշված օգտվողի անունը, գաղտնաբառը և օգտագործողի գործակալը.:

`medusa -M HTTP -h host -u {{username}} -p {{password}} -m USER-AGENT:"{{Agent}}"`

- Կիրառեք կոպիտ ուժ MySQL սերվերի դեմ՝ օգտագործելով օգտվողի անուններ և հեշ պարունակող ֆայլ.:

`medusa -M mysql -h host -U {{path/to/username_file}} -p {{hash}} -m PASS:HASH`

- Կիրառեք կոպիտ ուժ SMB սերվերների ցուցակի դեմ՝ օգտագործելով օգտվողի անունը և pwdump ֆայլը.:

`medusa -M smbnt -H {{path/to/hosts_file}} -C {{path/to/pwdump_file}} -u {{username}} -m PASS:HASH`
