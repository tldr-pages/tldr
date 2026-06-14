# sfdk cmake

> Կատարեք cmake-ի կառուցման քայլը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.cmake.adoc>:.

- Run cmake:

`sfdk cmake`

- Գործարկեք cmake-ը նշված նախագծի գրացուցակում.:

`sfdk cmake {{project}}`

- Գործարկել cmake-ը լրացուցիչ փաստարկներով.:

`sfdk cmake -- {{arguments}}`

- Գործարկեք cmake build-ը ընթացիկ գրացուցակում.:

`sfdk cmake --build .`

- Գործարկեք cmake build-ը ընթացիկ գրացուցակում լրացուցիչ cmake փաստարկներով.:

`sfdk cmake --build . {{cmake-arguments}}`

- Գործարկել cmake build-ը ընթացիկ գրացուցակում լրացուցիչ build գործիքի փաստարկներով.:

`sfdk cmake --build . -- {{build-tool-arguments}}`
