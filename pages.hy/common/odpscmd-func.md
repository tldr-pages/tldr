# odpscmd ֆունկցիա

> Կառավարեք գործառույթները ODPS-ում (Տվյալների մշակման բաց ծառայություն):.
> Տես նաև՝ `odpscmd`:.
> Լրացուցիչ տեղեկություններ. <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>:.

- [Ինտերակտիվ] Ցույց տալ գործառույթները ընթացիկ նախագծում.:

`list functions;`

- [Ինտերակտիվ] Ստեղծեք Java ֆունկցիա՝ օգտագործելով `.jar` ռեսուրսը.:

`create function {{func_name}} as {{path.to.package.Func}} using '{{package.jar}}';`

- [Ինտերակտիվ] Ստեղծեք Python ֆունկցիա՝ օգտագործելով `.py` ռեսուրսը.:

`create function {{func_name}} as {{script.Func}} using '{{script.py}}';`

- [Ինտերակտիվ] Ջնջել գործառույթը.:

`drop function {{func_name}};`
