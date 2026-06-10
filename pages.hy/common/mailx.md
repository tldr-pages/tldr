# mailx

> Ուղարկել և ստանալ նամակներ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/mailx>:.

- Ուղարկեք նամակ (բովանդակությունը պետք է մուտքագրվի հրամանից հետո և ավարտվի `<Ctrl d>`-ով):

`mailx {{[-s|--subject]}} "{{subject}}" {{to_addr}}`

- Ուղարկեք փոստ այլ հրամանից փոխանցված բովանդակությամբ.:

`echo "{{content}}" | mailx {{[-s|--subject]}} "{{subject}}" {{to_addr}}`

- Ուղարկեք նամակ ֆայլից կարդացված բովանդակությամբ.:

`mailx < {{content.txt}} {{[-s|--subject]}} "{{subject}}" {{to_addr}}`

- Նամակ ուղարկեք ստացողին և CC-ն մեկ այլ հասցեով.:

`mailx {{[-s|--subject]}} "{{subject}}" {{[-c|--cc]}} {{cc_addr}} {{to_addr}}`

- Ուղարկեք նամակ՝ նշելով ուղարկողի հասցեն.:

`mailx {{[-s|--subject]}} "{{subject}}" {{[-r|--from-address]}} {{from_addr}} {{to_addr}}`

- Նամակ ուղարկեք հավելվածով.:

`mailx {{[-a|--attach]}} {{path/to/file}} {{[-s|--subject]}} "{{subject}}" {{to_addr}}`
