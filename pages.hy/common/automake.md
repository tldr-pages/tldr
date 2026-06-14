#ավտոմեքենա

> Ավտոմատացված Makefile ստեղծում ծրագրային նախագծերի համար՝ օգտագործելով GNU ստանդարտները:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/automake/manual/automake.html#automake-Invocation>:.

- Գործարկեք automake-ը՝ `Makefile.am`-ը խմբագրելուց հետո Makefiles-ը վերականգնելու համար:

`automake`

- Ստեղծեք `Makefile.in` ոչ GNU նախագծի համար (օտար ռեժիմ).:

`automake --foreign`

- Վրիպազերծման համար ավելացրեք մանրամասն ելք.:

`automake {{[-v|--verbose]}}`

- Ավելացնել բացակայող ստանդարտ ֆայլեր (ՏԵՂԱԴՐՈՒՄ, ՊԱՏՃԱՌՈՒՄ, depcomp և այլն):

`automake {{[-a|--add-missing]}}`

- Ցուցադրել օգնությունը.:

`automake --help`
