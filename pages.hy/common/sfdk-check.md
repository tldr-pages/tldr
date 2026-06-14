# sfdk ստուգում

> Կատարել որակի ստուգումներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.cmake.adoc>:.

- Ցուցադրել թեստային փաթեթները.:

`sfdk check --list-suites`

- Գործարկել բոլոր կամ հիմնական թեստային փաթեթները.:

`sfdk check`

- Չեկին ավելացրեք փորձարկման մակարդակ.:

`sfdk check {{[-l|--levels]}} +{{level}}`

- Հեռացրեք փորձարկման մակարդակը ստուգումից.:

`sfdk check {{[-l|--levels]}} -{{level}}`

- Չեկին ավելացրեք թեստավորման հավաքածու.:

`sfdk check {{[-s|--suites]}} +{{suite}}`

- Հեռացրեք փորձարկման փաթեթը ստուգումից.:

`sfdk check {{[-s|--suites]}} -{{suite}}`
