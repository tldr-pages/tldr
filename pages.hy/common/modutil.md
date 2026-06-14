# մոդուտիլ

> Կառավարեք PKCS #11 մոդուլի տեղեկատվությունը ԱԱԾ անվտանգության մոդուլի տվյալների բազայում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/modutil>:.

- ԱԱԾ տվյալների բազայում ավելացրեք PKCS #11 մոդուլ (օրինակ՝ Firefox պրոֆիլ՝ `$HOME/.mozilla/firefox/default-release`):

`modutil -dbdir sql:{{path/to/nss_database_directory}} -add "{{module_label}}" -libfile {{path/to/pkcs11_mod.so}}`

- Թվարկեք PKCS #11 մոդուլները ԱՎԾ տվյալների բազայում.:

`modutil -dbdir sql:{{path/to/nss_database_directory}} -list`
