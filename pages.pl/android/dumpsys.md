# dumpsys

> Uzyskaj informacje o usługach systemu Android.
> Ta komenda może być używana tylko poprzez `adb shell`.
> Więcej informacji: <https://developer.android.com/tools/dumpsys>.

- Uzyskaj dane diagnostyczne dla wszystkich usług systemowych:

`dumpsys`

- Uzyskaj dane diagnostyczne dla określonej usługi systemowej:

`dumpsys {{usługa}}`

- Wypisz wszystkie usługi, o których `dumpsys` może podać informacje:

`dumpsys -l`

- Wypisz argumenty specyficzne dla danej usługi:

`dumpsys {{usługa}} -h`

- Wyklucz określoną usługę z wyjścia diagnostycznego:

`dumpsys --skip {{usługa}}`

- Określ czas oczekiwania w sekundach (domyślnie 10s):

`dumpsys -t {{8}}`
