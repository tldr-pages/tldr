# git գաղտնիք

> Պահպանում է անձնական տվյալները Git պահեստում: Գրված է Բաշում։
> Լրացուցիչ տեղեկություններ. <https://github.com/sobolevn/git-secret>:.

- Նախաձեռնեք `git-secret`-ը տեղական պահոցում՝:

`git secret init`

- Մուտք տրամադրեք Git-ի ընթացիկ օգտատիրոջ էլ.:

`git secret tell -m`

- Տրամադրել մուտքը էլեկտրոնային փոստով.:

`git secret tell {{email}}`

- Չեղարկել մուտքը էլեկտրոնային փոստով.:

`git secret killperson {{email}}`

- Գաղտնիքների հասանելիությամբ էլ.:

`git secret whoknows`

- Գրանցեք գաղտնի ֆայլ.:

`git secret add {{path/to/file}}`

- Գաղտնագրեք գաղտնիքները.:

`git secret hide`

- Գաղտնի ֆայլերի գաղտնազերծում.:

`git secret reveal`
