# dumpsys

> Dostarczanie informacji o usługach systemu Android.
> Ta komenda może być używana tylko poprzez `adb shell`.
> Więcej informacji: <https://developer.android.com/tools/dumpsys>.

- Uzyskaj dane diagnostyczne dla wszystkich usług systemowych:

`dumpsys`

- Uzyskaj dane diagnostyczne dla określonej usługi systemowej:

`dumpsys {{usługa}}`

- Lista wszystkich usług, o których `dumpsys` może dać informacje:

`dumpsys -l`

- Lista argumentów specyficznych dla usługi:

`dumpsys {{usługa}} -h`

- Wykluczenie określonej usługi z wyjścia diagnostycznego:

`dumpsys --skip {{usługa}}`

- Określenie czasu oczekiwania w sekundach (domyślnie 10s):

`dumpsys -t {{sekundy}}`
