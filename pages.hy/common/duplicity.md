# երկակիություն

> Ստեղծեք աստիճանական, սեղմված, կոդավորված և տարբերակված կրկնօրինակներ:.
> Կարող է նաև կրկնօրինակները վերբեռնել մի շարք backend ծառայություններում:.
> Նշում․ կախված տարբերակից՝ որոշ տարբերակներ կարող են հասանելի չլինել (օրինակ՝ `--gio` 2.0.0-ում):.
> Լրացուցիչ տեղեկություններ. <https://duplicity.gitlab.io/stable/duplicity.1.html#name>:.

- Կրկնօրինակեք գրացուցակը FTPS-ի միջոցով հեռավոր մեքենայի վրա՝ գաղտնագրելով այն գաղտնաբառով.:

`FTP_PASSWORD={{ftp_login_password}} PASSPHRASE={{encryption_password}} duplicity {{path/to/source_directory}} {{ftps://user@hostname/path/to/target_directory}}/`

- Կրկնօրինակեք գրացուցակը Amazon S3-ում՝ ամեն ամիս կատարելով ամբողջական կրկնօրինակում.:

`duplicity --full-if-older-than {{1M}} s3://{{bucket_name[/prefix]}}`

- Ջնջեք 1 տարուց ավելի հին տարբերակները WebDAV բաժնետոմսում պահված կրկնօրինակից.:

`FTP_PASSWORD={{webdav_login_password}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://user@hostname[:port]/some_directory}}`

- Թվարկեք առկա կրկնօրինակները.:

`duplicity collection-status "file://{{absolute/path/to/backup_directory}}"`

- Թվարկեք ֆայլերը հեռավոր մեքենայի վրա պահված կրկնօրինակում SSH-ի միջոցով.:

`duplicity list-current-files {{[-t|--time]}} {{YYYY-MM-DD}} scp://{{user@hostname}}/{{path/to/backup_directory}}`

- Վերականգնել ենթատեղեկատուը GnuPG-ով կոդավորված տեղական կրկնօրինակից տվյալ վայրում.:

`PASSPHRASE={{gpg_key_password}} duplicity restore --encrypt-key {{gpg_key_id}} --path-to-restore {{path/to/restore_directory}} file://{{absolute/path/to/backup_directory}} {{path/to/directory_to_restore_to}}`
