# dcfldd

> dd-ի ընդլայնված տարբերակը դատական փորձաքննության և անվտանգության համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/dcfldd>:.

- Պատճենեք սկավառակը չմշակված պատկերի ֆայլում և հաշեք պատկերը՝ օգտագործելով SHA256:

`dcfldd if={{/dev/disk_device}} of={{file.img}} hash=sha256 hashlog={{file.hash}}`

- Պատճենեք սկավառակը չմշակված պատկերի ֆայլում՝ հեշելով յուրաքանչյուր 1 ԳԲ հատվածը.:

`dcfldd if={{/dev/disk_device}} of={{file.img}} hash={{sha512|sha384|sha256|sha1|md5}} hashlog={{file.hash}} hashwindow={{1G}}`
