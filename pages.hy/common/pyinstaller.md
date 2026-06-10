# pyinstaller

> Փաթեթավորեք Python հավելվածը և դրա կախվածությունները մեկ փաթեթի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://pyinstaller.org/en/stable/man/pyinstaller.html>:.

- Փաթեթավորեք Python սկրիպտը մեկ թղթապանակով փաթեթի մեջ (արդյունքը գնում է `dist/`):

`pyinstaller {{path/to/script.py}}`

- Փաթեթավորեք Python սցենարը մեկ գործարկվող ֆայլի մեջ.:

`pyinstaller {{[-F|--onefile]}} {{path/to/script.py}}`

- Փաթեթավորեք GUI հավելված՝ առանց վահանակի պատուհան բացելու.:

`pyinstaller {{[-w|--windowed]}} {{path/to/script.py}}`

- Սահմանեք փաթեթավորված գործադիրի անունը.:

`pyinstaller {{[-n|--name]}} {{app_name}} {{path/to/script.py}}`

- Սահմանեք գործարկվողի համար հատուկ պատկերակ.:

`pyinstaller {{[-i|--icon]}} {{path/to/icon.ico}} {{path/to/script.py}}`

- Ներառեք լրացուցիչ տվյալների ֆայլեր կամ գրացուցակներ փաթեթում.:

`pyinstaller --add-data "{{path/to/source}}:{{destination}}" {{path/to/script.py}}`

- Ցուցադրել օգնությունը.:

`pyinstaller {{[-h|--help]}}`

- Ցուցադրման տարբերակը:

`pyinstaller {{[-v|--version]}}`
