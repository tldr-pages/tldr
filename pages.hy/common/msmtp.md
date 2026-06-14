# msmtp

> SMTP հաճախորդ:.
> Այն կարդում է տեքստ `stdin`-ից և ուղարկում այն ​​SMTP սերվերին:.
> Լրացուցիչ տեղեկություններ. <https://marlam.de/msmtp/>:.

- Ուղարկեք նամակ՝ օգտագործելով `~/.msmtprc`-ում կազմաձևված կանխադրված հաշիվը՝:

`echo "{{Hello world}}" | msmtp {{to@example.org}}`

- Ուղարկեք նամակ՝ օգտագործելով `~/.msmtprc`-ում կազմաձևված հատուկ հաշիվ՝:

`echo "{{Hello world}}" | msmtp --account={{account_name}} {{to@example.org}}`

- Ուղարկեք նամակ առանց կազմաձևված հաշվի: Գաղտնաբառը պետք է նշվի `~/.msmtprc` ֆայլում՝:

`echo "{{Hello world}}" | msmtp --host={{localhost}} --port={{999}} --from={{from@example.org}} {{to@example.org}}`
