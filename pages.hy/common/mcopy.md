# mcopy

> Պատճենել MSDOS ֆայլերը Unix-ում/ից:.
> `mtools` փաթեթի մի մասը:.
> Նշում. DOS-ի ենթադիրեկտորիաներին անդրադառնալու համար օգտագործեք առաջ շեղ (`/`)՝ հակադարձի փոխարեն (`\`):.
> Լրացուցիչ տեղեկություններ. <https://gnu.org/software/mtools/manual/mtools.html#mcopy>:.

- Պատճենեք ֆայլը Linux-ից MS-DOS սկավառակի կամ պատկերի վրա.:

`mcopy {{path/to/source_file}} {{A}}:/{{path/to/target_file}}`

- Պատճենեք ֆայլը MS-DOS սկավառակից ընթացիկ Linux գրացուցակում.:

`mcopy {{A}}:{{/path/to/source_file}} .`

- Պատճենեք բոլոր ֆայլերը MS-DOS սկավառակից Linux գրացուցակ.:

`mcopy {{A}}: {{path/to/target_directory}}`

- Պատճենեք ֆայլը DOS սկավառակի մեջ [i]mage ֆայլ՝ դրայվի տառի փոխարեն (`::` ներկայացնում է DOS սկավառակի արմատային գրացուցակը):

`mcopy -i {{path/to/image.img}} {{path/to/source_file}} ::/{{path/to/target_file}}`

- Պատճենեք ֆայլը սկավառակի պատկերից ընթացիկ գրացուցակում.:

`mcopy -i {{path/to/image.img}} ::/{{path/to/source_file}} .`

- Պատճենեք գրացուցակը կրկնվող MS-DOS սկավառակի վրա.:

`mcopy -s {{path/to/source_directory}} {{A}}:/{{path/to/target_directory}}`

- Պատճենեք ֆայլը և [p]պահեք ատրիբուտները.:

`mcopy -p {{path/to/source_file}} {{A}}:/{{path/to/target_file}}`
