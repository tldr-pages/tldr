# git hash-object

> Հաշվում է բովանդակության եզակի հեշ բանալին և ընտրովի ստեղծում նշված տիպով օբյեկտ:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-hash-object>:.

- Հաշվեք օբյեկտի ID-ն առանց այն պահելու.:

`git hash-object {{path/to/file}}`

- Հաշվեք օբյեկտի ID-ն և պահեք այն Git տվյալների բազայում.:

`git hash-object -w {{path/to/file}}`

- Հաշվեք օբյեկտի ID-ն՝ նշելով օբյեկտի տեսակը.:

`git hash-object -t {{blob|commit|tag|tree}} {{path/to/file}}`

- Հաշվեք օբյեկտի ID-ն `stdin`-ից.:

`cat {{path/to/file}} | git hash-object --stdin`
