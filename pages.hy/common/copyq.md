# copyq

> Clipboard-ի կառավարիչ՝ առաջադեմ գործառույթներով:.
> Լրացուցիչ տեղեկություններ. <https://copyq.readthedocs.io/en/latest/command-line.html>:.

- Գործարկեք CopyQ՝ սեղմատախտակի պատմությունը պահելու համար.:

`copyq`

- Ցույց տալ ընթացիկ clipboard բովանդակությունը:

`copyq clipboard`

- Տեղադրեք չմշակված տեքստը clipboard պատմության մեջ.:

`copyq add -- {{text1}} {{text2}} {{text3}}`

- Տեղադրեք տեքստ, որը պարունակում է փախուստի հաջորդականություններ ('\n', '\t') clipboard պատմության մեջ.:

`copyq add {{firstline\nsecondline}}`

- Տպեք clipboard պատմության առաջին 3 տարրերի բովանդակությունը.:

`copyq read 0 1 2`

- Պատճենեք ֆայլի բովանդակությունը clipboard-ում.:

`copyq < {{path/to/file.txt}} copy`

- Պատճենեք JPEG պատկերը clipboard-ում.:

`copyq < {{path/to/image.jpg}} copy image/jpeg`
