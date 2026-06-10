# աղբարկղ

> Ցանցային երթևեկության աղբահանության գործիք:.
> Լրացուցիչ տեղեկություններ. <https://www.wireshark.org/docs/man-pages/dumpcap.html>:.

- Ցուցադրել հասանելի միջերեսները.:

`dumpcap {{[-D|--list-interfaces]}}`

- Փաթեթներ գրավել հատուկ ինտերֆեյսի վրա.:

`dumpcap {{[-i|--interface]}} {{1}}`

- Փաթեթները գրավել որոշակի վայրում.:

`dumpcap {{[-i|--interface]}} {{1}} -w {{path/to/output_file.pcapng}}`

- Գրեք օղակի բուֆերում՝ որոշակի չափի ֆայլի որոշակի առավելագույն սահմանաչափով.:

`dumpcap {{[-i|--interface]}} {{1}} -w {{path/to/output_file.pcapng}} {{[-b|--ring-buffer]}} filesize:{{500000}} {{[-b|--ring-buffer]}} files:{{10}}`
