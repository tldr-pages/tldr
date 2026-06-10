# dosbox

> MS-DOS էմուլյատոր՝ հին DOS հավելվածներն ու խաղերը գործարկելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.dosbox.com/wiki/Usage>:.

- Սկսեք DOSBox-ը լռելյայն կարգավորումներով.:

`dosbox`

- Գործարկեք DOS գործարկիչը, որը գտնվում է որոշակի ուղու վրա.:

`dosbox {{path/to/executable.exe}}`

- Տեղադրեք թղթապանակը որպես C: և գործարկեք գործարկվողը.:

`dosbox {{path/to/executable.exe}} -c "MOUNT C {{path/to/folder}}"`

- Գործարկեք DOSBox-ը լիաէկրան ռեժիմով.:

`dosbox -fullscreen`

- Ծրագրի գործարկումից հետո ավտոմատ դուրս եկեք DOSBox-ից.:

`dosbox {{path/to/executable.exe}} -exit`
