# aspell

> Ինտերակտիվ ուղղագրության ստուգիչ:.
> Լրացուցիչ տեղեկություններ. <http://aspell.net/man-html/index.html>:.

- Ուղղագրության ստուգում մեկ ֆայլ.:

`aspell check {{path/to/file}}`

- Թվարկե՛ք `stdin`-ից սխալ գրված բառերը՝:

`cat {{path/to/file}} | aspell list`

- Ցույց տալ հասանելի բառարանային լեզուները.:

`aspell dicts`

- Գործարկեք `aspell`-ը այլ լեզվով (ընդունում է երկու տառ ISO 639 լեզվի կոդը).:

`aspell --lang {{cs}}`

- Թվարկեք `stdin`-ից սխալ գրված բառերը և անտեսեք բառերը անձնական բառերի ցանկից:

`cat {{path/to/file}} | aspell --personal {{personal-word-list.pws}} list`
