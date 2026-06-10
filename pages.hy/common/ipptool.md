# ipptool

> Թողարկեք IPP հարցումներ և ստացեք տպիչի/սերվերի պատասխանները:.
> Տես նաև՝ `ippfind`, `ippeveprinter`:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-ipptool.html>:.

- Ստացեք բոլոր հատկանիշները և դրանց արժեքները, որոնք աջակցվում են տպիչի կողմից.:

`ipptool ipp://{{printer_uri}} get-completed-jobs.test`

- Ստացեք տպիչի ավարտված աշխատանքների ցանկը.:

`ipptool ipp://{{printer_uri}} get-completed-jobs.test`

- Ուղարկեք էլփոստի ծանուցում, երբ տպիչը փոխվում է.:

`ipptool -d recipient=mailto:{{email}} ipp://{{printer_uri}} create-printer-subscription.test`
