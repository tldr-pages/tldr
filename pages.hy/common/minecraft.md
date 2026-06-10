# Minecraft

> Գործարկեք անգլուխ Minecraft սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://minecraft.wiki/w/Tutorial:Setting_up_a_Java_Edition_server>:.

- Սկսեք Minecraft սերվեր և ստեղծեք աշխարհ, եթե այն գոյություն չունի.:

`java -jar {{path/to/server.jar}} --nogui`

- Սահմանեք հիշողության նվազագույն և առավելագույն քանակը, որը թույլատրվում է ունենալ սերվերին (Նշում. դրանց նույն կարգավորումը կանխում է կույտային մասշտաբով առաջացած հետաձգումը).:

`java -Xms{{1024M}} -Xmx{{2048M}} -jar {{path/to/server.jar}} --nogui`

- Սկսեք սերվեր GUI-ով.:

`java -jar {{path/to/server.jar}}`

- [Ինտերակտիվ] Անջատեք սերվերը.:

`stop`
