# zstyle

> Սահմանեք և որոնեք կազմաձևման ոճերը Zsh-ում:.
> Այս ներկառուցվածը `zsh/zutil` մոդուլի մի մասն է:.
> Լրացուցիչ տեղեկություններ. <https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html>:.

- Նշեք բոլոր սահմանված ոճերը.:

`zstyle`

- Նշեք ոճերը որպես պատրաստ տեղադրելու `zstyle` հրամաններ.:

`zstyle -L`

- Սահմանեք ոճ կոնկրետ օրինակի համար.:

`zstyle {{pattern}} {{style}} {{value1 value2...}}`

- Ջնջել ոճը կոնկրետ օրինակի համար.:

`zstyle -d {{pattern}}`

- Ստացեք ոճի արժեքը որպես տող փոփոխականի մեջ.:

`zstyle -s {{context}} {{style}} {{variable_name}}`

- Ստացեք ոճի արժեքը որպես բուլյան փոփոխականի մեջ.:

`zstyle -b {{context}} {{style}} {{variable_name}}`

- Ստացեք ոճի արժեքը որպես զանգված.:

`zstyle -a {{context}} {{style}} {{variable_name}}`
