# pio տուն

> Գործարկեք PlatformIO Home վեբ սերվերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>:.

- Բացեք PlatformIO Home-ը լռելյայն վեբ դիտարկիչում.:

`pio home`

- Օգտագործեք հատուկ HTTP պորտ (կանխադրված է 8008):

`pio home --port {{port}}`

- Կապվել որոշակի IP հասցեի հետ (կանխադրված է 127.0.0.1):

`pio home --host {{ip_address}}`

- Ավտոմատ մի բացեք PlatformIO Home-ը լռելյայն վեբ դիտարկիչում.:

`pio home --no-open`

- Ավտոմատ անջատել սերվերը ժամանակի վերջում (վայրկյաններով), երբ որևէ հաճախորդ միացված չէ.:

`pio home --shutdown-timeout {{time}}`

- Նշեք նստաշրջանի եզակի նույնացուցիչ՝ PlatformIO Home-ն այլ օրինակներից մեկուսացված և երրորդ կողմի մուտքից պաշտպանված պահելու համար.:

`pio home --session-id {{id}}`
