# xmake

> Lua-ի վրա հիմնված C & C++ կառուցման միջպլատֆորմային ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://xmake.io/#/getting_started>:.

- Ստեղծեք Xmake C նախագիծ, որը բաղկացած է բարև աշխարհից և `xmake.lua`-ից՝:

`xmake create {{[-l|--language]}} {{[c|clean]}} {{[-P|--project]}} {{project_name}}`

- Կառուցեք և գործարկեք Xmake նախագիծ.:

`xmake {{[b|build]}} {{[r|run]}}`

- Անմիջապես գործարկեք կազմված Xmake թիրախը.:

`xmake {{[r|run]}} {{target_name}}`

- Կազմաձևեք նախագծի կառուցման թիրախները.:

`xmake {{[f|config]}} {{[-p |--plat=]}}{{macosx|linux|iphoneos|...}} {{[-a |--arch=]}}{{x86_64|i386|arm64|...}} {{[-m |--mode=]}}{{debug|release}}`

- Տեղադրեք կազմված թիրախը գրացուցակում.:

`xmake {{[i|install]}} {{[-o |--installdir=]}}{{path/to/directory}}`
