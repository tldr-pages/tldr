# cppclean

> Գտեք չօգտագործված կոդը C++ նախագծերում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/myint/cppclean>:.

- Գործարկել նախագծի գրացուցակում.:

`cppclean {{path/to/project}}`

- Գործարկել մի նախագծի վրա, որտեղ վերնագրերը գտնվում են `inc1/` և `inc2/` գրացուցակներում.:

`cppclean {{path/to/project}} --include-path {{inc1}} --include-path {{inc2}}`

- Գործարկել որոշակի ֆայլ `main.cpp`:

`cppclean {{main.cpp}}`

- Գործարկել ընթացիկ գրացուցակում, բացառելով «build» գրացուցակը.:

`cppclean {{.}} --exclude {{build}}`
