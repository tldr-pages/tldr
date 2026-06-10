# weasyprint

> Տրամադրել HTML-ը PDF կամ PNG:.
> Լրացուցիչ տեղեկություններ. <https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#command-line-api>:.

- Ներկայացրեք HTML ֆայլը PDF.:

`weasyprint {{path/to/input.html}} {{path/to/output.pdf}}`

- Ներկայացրեք HTML ֆայլը PNG-ին, ներառյալ լրացուցիչ օգտվողի ոճաթերթը.:

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --stylesheet {{path/to/stylesheet.css}}`

- Արտադրել վրիպազերծման լրացուցիչ տեղեկատվություն՝:

`weasyprint {{path/to/input.html}} {{path/to/output.pdf}} --verbose`

- PNG-ին արտածելիս նշեք հատուկ լուծում.:

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --resolution {{300}}`

- Մուտքային HTML ֆայլում նշեք բազային URL հարաբերական URL-ների համար.:

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --base-url {{url_or_filename}}`
