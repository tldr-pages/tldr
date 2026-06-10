# աղ-կանչ

> Աղի աղի աղիի մինիոնի վրա տեղական աղը կանչեք:.
> Լրացուցիչ տեղեկություններ. <https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>:.

- Կատարեք բարձր մակարդակ այս մինիոնի վրա.:

`salt-call state.highstate`

- Կատարեք բարձր վիճակի չոր գործարկում, հաշվարկեք բոլոր փոփոխությունները, բայց իրականում մի կատարեք դրանք.:

`salt-call state.highstate test=true`

- Կատարեք բարձր մակարդակ՝ բացահայտ վրիպազերծման ելքով.:

`salt-call {{[-l|--log-level]}} debug state.highstate`

- Թվարկե՛ք այս մինիոնի հատիկները.:

`salt-call grains.items`
