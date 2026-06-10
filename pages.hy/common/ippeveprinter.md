# ippeveprinter

> Պարզ IPP Everywhere տպիչ սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-ippeveprinter.html>:.

- Գործարկեք սերվերը հատուկ ծառայության անունով.:

`ippeveprinter "{{service_name}}"`

- Բեռնել տպիչի հատկանիշները PPD ֆայլից.:

`ippeveprinter -P {{path/to/file.ppd}} "{{service_name}}"`

- Գործարկեք `file` հրամանը, երբ աշխատանք ուղարկվում է սերվերին.:

`ippeveprinter -c {{/usr/bin/file}} "{{service_name}}"`

- Նշեք գրացուցակը, որը կպահի տպագրված ֆայլերը (ըստ լռելյայն՝ տեղեկատու՝ օգտվողի ժամանակավոր գրացուցակի տակ).:

`ippeveprinter -d {{spool_directory}} "{{service_name}}"`

- Պահեք տպագիր փաստաթղթերը spool գրացուցակում, այլ ոչ թե ջնջեք դրանք.:

`ippeveprinter -k "{{service_name}}"`

- Նշեք տպիչի արագությունը էջերով/րոպե միավորով (կանխադրված 10).:

`ippeveprinter -s {{speed}} "{{service_name}}"`
