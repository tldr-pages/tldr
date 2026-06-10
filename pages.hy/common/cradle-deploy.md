# օրորոցի տեղակայում

> Կառավարեք Cradle-ի տեղակայումները:.
> Լրացուցիչ տեղեկություններ. <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>:.

- Տեղադրեք Cradle-ը սերվերի վրա.:

`cradle deploy production`

- Տեղադրեք ստատիկ ակտիվներ Amazon S3-ում.:

`cradle deploy s3`

- Տեղադրեք ստատիկ ակտիվներ, ներառյալ Yarn «բաղադրիչները» գրացուցակը.:

`cradle deploy s3 --include-yarn`

- Տեղադրեք ստատիկ ակտիվներ, ներառյալ «վերբեռնման» գրացուցակը.:

`cradle deploy s3 --include-upload`
