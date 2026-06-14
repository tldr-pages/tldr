# կախարդական ներմուծում

> Լուսանկարեք X սերվերի էկրանի մի մասը կամ ամբողջը և պահեք պատկերը ֆայլում:.
> Տես նաև՝ `magick`:.
> Լրացուցիչ տեղեկություններ. <https://imagemagick.org/script/import.php>:.

- Գրեք ամբողջ X սերվերի էկրանը PostScript ֆայլի մեջ.:

`magick import -window root {{path/to/output.ps}}`

- Հեռավոր X սերվերի էկրանի բովանդակությունը նկարեք PNG պատկերի մեջ.:

`magick import -window root -display {{remote_host}}:{{screen}}.{{display}} {{path/to/output.png}}`

- Լուսանկարեք որոշակի պատուհան՝ հաշվի առնելով դրա ID-ն, ինչպես ցուցադրվում է `xwininfo`-ով JPEG պատկերի մեջ.:

`magick import -window {{window_id}} {{path/to/output.jpg}}`
