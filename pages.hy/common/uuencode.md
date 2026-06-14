# uuecod

> Կոդավորեք երկուական ֆայլերը ASCII-ի մեջ՝ փոխադրելու համար այն միջավայրերի միջոցով, որոնք աջակցում են միայն պարզ ASCII կոդավորումը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/uuencode>:.

- Կոդավորեք ֆայլը և տպեք արդյունքը `stdout`-ում:

`uuencode {{path/to/input_file}} {{output_file_name_after_decoding}}`

- Կոդավորեք ֆայլը և արդյունքը գրեք ֆայլում.:

`uuencode -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`

- Կոդավորեք ֆայլը, օգտագործելով Base64-ը, կանխադրված uuecode կոդավորման փոխարեն և արդյունքը գրեք ֆայլում.:

`uuencode {{[-m|--base64]}} -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`
