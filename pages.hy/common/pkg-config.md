# pkg-config

> Տրամադրել հավելվածների կազմման համար տեղադրված գրադարանների մանրամասները:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pkg-config>:.

- Ստացեք գրադարանների ցանկը և դրանց կախվածությունը.:

`pkg-config --libs {{library1 library2 ...}}`

- Ստացեք գրադարանների ցանկը, դրանց կախվածությունները և gcc-ի պատշաճ cflag-ները.:

`pkg-config --cflags --libs {{library1 library2 ...}}`

- Կազմեք ձեր կոդը libgtk-3, libwebkit2gtk-4.0 և նրանց բոլոր կախվածությունների հետ.:

`c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example`
