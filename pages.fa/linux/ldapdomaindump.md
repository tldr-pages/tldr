# ldapdomaindump

> استخراج اطلاعات کاربران، رایانه‌ها، گروه‌ها، سیستم‌عامل و عضویت از طریق LDAP در قالب HTML، JSON و خروجی قابل جست‌وجو با grep.
> همچنین : `ldapsearch`.
> اطلاعات بیشتر: <https://github.com/dirkjanm/ldapdomaindump#usage>.

- استخراج همهٔ اطلاعات با حساب LDAP مشخص:

`ldapdomaindump {{[-u|--user]}} {{domain}}\{{username}} {{[-p|--password]}} {{password|ntlm_hash}} {{hostname|ip}}`

- استخراج همهٔ اطلاعات همراه با حل نام میزبان رایانه‌ها:

`ldapdomaindump {{[-r|--resolve]}} {{[-u|--user]}} {{domain}}\{{username}} {{[-p|--password]}}{{password}} {{hostname|ip}}`

- استخراج همهٔ اطلاعات همراه با حل نام میزبان رایانه‌ها توسط سرور DNS انتخاب‌شده:

`ldapdomaindump {{[-r|--resolve]}} {{[-n|--dns-server]}} {{domain_controller_ip}} {{[-u|--user]}} {{domain}}\{{username}} {{[-p|--password]}}{{password}} {{hostname|ip}}`

- استخراج همهٔ اطلاعات در دایرکتوری مشخص بدون خروجی JSON:

`ldapdomaindump --no-json {{[-o|--outdir]}} {{path/to/directory}} {{[-u|--user]}} {{domain}}\{{username}} {{[-p|--password]}}{{password}} {{hostname|ip}}`
