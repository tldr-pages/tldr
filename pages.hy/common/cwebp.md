# cwebp

> Կոմպրես պատկերի ֆայլը WebP ֆայլի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://developers.google.com/speed/webp/docs/cwebp>:.

- Կոմպրես WebP ֆայլը լռելյայն կարգավորումներով (կորուստ սեղմում, q = 75) [o]utput ֆայլում.:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}}`

- Կոմպրես WebP ֆայլը լավագույն կորուստով սեղմման [q] որակով և ֆայլի ամենամեծ չափով.:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{100}}`

- Կոմպրես WebP ֆայլը վատթարագույն կորստի սեղմման [q] որակով և ֆայլի ամենափոքր չափով.:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{0}}`

- Կոմպրես WebP ֆայլը անկորուստ սեղմումով և ամենափոքր հնարավոր ֆայլի չափով.:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -z 9`

- Սեղմեք WebP ֆայլը և չափափոխեք պատկերի վրա (եթե լայնությունը կամ բարձրությունը 0 են, մասշտաբը պահպանում է կողմերի հարաբերակցությունը).:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -resize {{width}} {{height}}`

- Սեղմեք WebP ֆայլը և թողեք ալֆա ալիքի տեղեկատվությունը.:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -noalpha`
