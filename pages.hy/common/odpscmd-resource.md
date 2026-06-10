# odpscmd ռեսուրս

> Կառավարեք ռեսուրսները ODPS-ում (Տվյալների մշակման բաց ծառայություն):.
> Տես նաև՝ `odpscmd`:.
> Լրացուցիչ տեղեկություններ. <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>:.

- [Ինտերակտիվ] Ցույց տալ ռեսուրսները ընթացիկ նախագծում.:

`list resources;`

- [Ինտերակտիվ] Ավելացնել ֆայլի ռեսուրս.:

`add file {{filename}} as {{alias}};`

- [Ինտերակտիվ] Ավելացնել արխիվային ռեսուրս.:

`add archive {{archive.tar.gz}} as {{alias}};`

- [Ինտերակտիվ] Ավելացնել `.jar` ռեսուրս՝:

`add jar {{package.jar}};`

- [Ինտերակտիվ] Ավելացնել `.py` ռեսուրս՝:

`add py {{script.py}};`

- [Ինտերակտիվ] Ջնջել ռեսուրսը.:

`drop resource {{resource_name}};`
