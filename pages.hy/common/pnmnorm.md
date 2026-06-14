# pnmnorm

> Նորմալացրեք հակադրությունը PNM պատկերում:.
> Տես նաև՝ `pnmhisteq`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmnorm.html>:.

- Ստիպեք ամենապայծառ պիքսելներին լինել սպիտակ, ամենամուգ պիքսելներին՝ սև և գծային կերպով տարածեք դրանց միջև եղածները.:

`pnmnorm {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Ստիպեք ամենապայծառ պիքսելներին լինել սպիտակ, ամենամուգ պիքսելներին՝ սև և տարածեք դրանց միջև ընկած հատվածները այնպես, որ `n` պայծառություն ունեցող պիքսելները դառնան 50% պայծառ:

`pnmnorm {{[-midv|-midvalue]}} {{n}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Պահպանեք պիքսելների երանգը, փոփոխեք միայն պայծառությունը.:

`pnmnorm {{[-k|-keephues]}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Նշեք պիքսելի պայծառությունը հաշվարկելու մեթոդ.:

`pnmnorm -{{luminosity|colorvalue|saturation}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
