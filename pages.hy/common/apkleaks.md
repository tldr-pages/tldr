# apkleaks

> Բացահայտեք URI-ները, վերջնակետերը և գաղտնիքները APK ֆայլերից:.
> Նշում. APKLeaks-ն օգտագործում է `jadx` ապամոնտաժիչը՝ APK ֆայլերը ապակոմպիլացնելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/dwisiswant0/apkleaks>:.

- Սկանավորեք APK ֆայլը URI-ների, վերջնակետերի և գաղտնիքների համար.:

`apkleaks {{[-f|--file]}} {{path/to/file}}.apk`

- Սկանավորեք և պահպանեք ելքը որոշակի ֆայլում.:

`apkleaks {{[-f|--file]}} {{path/to/file}}.apk {{[-o|--output]}} {{path/to/output.txt}}`

- Անցեք `jadx` ապամոնտաժող փաստարկները.:

`apkleaks {{[-f|--file]}} {{path/to/file}}.apk {{[-a|--args]}} "{{--threads-count 5 --deobf}}"`
