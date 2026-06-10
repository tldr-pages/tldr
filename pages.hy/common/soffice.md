#օֆիս

> CLI հզոր և անվճար LibreOffice փաթեթի համար:.
> Լրացուցիչ տեղեկություններ. <https://help.libreoffice.org/latest/en-US/text/shared/guide/pdf_params.html>:.

- Բացեք մեկ կամ մի քանի ֆայլ միայն կարդալու ռեժիմով.:

`soffice --view {{path/to/file1 path/to/file2 ...}}`

- Ցուցադրել մեկ կամ մի քանի ֆայլերի բովանդակությունը.:

`soffice --cat {{path/to/file1 path/to/file2 ...}}`

- Տպել ֆայլերը հատուկ տպիչի միջոցով.:

`soffice --pt {{printer_name}} {{path/to/file1 path/to/file2 ...}}`

- Փոխակերպեք ընթացիկ գրացուցակի բոլոր `.doc` ֆայլերը PDF-ի.:

`soffice --convert-to pdf *.doc`
