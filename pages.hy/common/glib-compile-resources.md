# glib-compile-resources

> Կազմում է ռեսուրսների ֆայլերը (օրինակ՝ պատկերները) երկուական ռեսուրսների փաթեթի մեջ:.
> Սրանք կարող են կապված լինել GTK հավելվածների հետ՝ օգտագործելով GResource API-ը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/glib-compile-resources>:.

- Կազմեք `file.gresource.xml`-ում նշված ռեսուրսները `.gresource` երկուականին.:

`glib-compile-resources {{file.gresource.xml}}`

- Կազմեք `file.gresource.xml`-ում նշված ռեսուրսները C աղբյուրի ֆայլին՝:

`glib-compile-resources --generate-source {{file.gresource.xml}}`

- Կազմեք ռեսուրսները `file.gresource.xml`-ով ընտրված թիրախային ֆայլում՝ `.c`, `.h` կամ `.gresource` ընդլայնմամբ:

`glib-compile-resources --generate --target={{file.ext}} {{file.gresource.xml}}`

- Տպեք `file.gresource.xml`-ում նշված ռեսուրսների ֆայլերի ցանկը՝:

`glib-compile-resources --generate-dependencies {{file.gresource.xml}}`
