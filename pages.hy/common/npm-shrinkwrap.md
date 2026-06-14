# npm նեղանալ

> Կողպեք փաթեթի կախվածությունը՝ ստեղծելով `npm-shrinkwrap.json` ֆայլ:.
> Նման է `package-lock.json`-ին, բայց նախատեսված է հրապարակված փաթեթների համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/shrinkwrap/>:.

- Ստեղծեք `npm-shrinkwrap.json` ֆայլ ընթացիկ `package-lock.json`-ից:

`npm shrinkwrap`

- Գործարկել արտադրության ռեժիմում (բացառում է devDependencies):

`npm shrinkwrap --production`

- Ստիպեք վերստեղծել shrinkwrap ֆայլը, նույնիսկ եթե այն արդեն գոյություն ունի.:

`npm shrinkwrap --force`
