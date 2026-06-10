# ctest

> CMake թեստային վարորդի ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.kitware.com/cmake/community/-/wikis/doc/ctest/Testing-With-CTest>:.

- Գործարկեք բոլոր թեստերը ընթացիկ CMake build գրացուցակում.:

`ctest`

- Գործարկեք CMake build գրացուցակում սահմանված բոլոր թեստերը՝ միաժամանակ կատարելով 4 [j]obs:

`ctest {{[-j|--parallel]}} 4`

- Գործարկեք բոլոր թեստերը, որոնք սահմանված են CMake build գրացուցակում և տպեք մանրամասն տեղեկամատյաններ ձախողված թեստերի վրա.:

`ctest --output-on-failure`

- Թվարկեք առկա թեստերը.:

`ctest {{[-N|--show-only]}}`

- Կատարեք մեկ թեստ՝ հիմնվելով դրա անվան վրա, կամ զտեք `regex`-ով:

`ctest --output-on-failure {{[-R|--tests-regex]}} '^{{test_name}}$'`
