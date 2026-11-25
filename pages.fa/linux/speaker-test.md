# speaker-test

> تولیدکنندهٔ صدای آزمون بلندگو برای ALSA.
> همچنین ببینید: `aplay`, `arecord`, `amixer`.
> اطلاعات بیشتر: <https://manned.org/speaker-test>.

- آزمودن بلندگوهای پیش‌فرض با نویز صورتی:

`speaker-test`

- آزمودن بلندگوهای پیش‌فرض با فایل WAV ازپیش‌تعریف‌شده:

`speaker-test {{[-t|--test]}} wav`

- آزمودن پیکربندی بلندگوهای چندکاناله:

`speaker-test {{[-t|--test]}} wav {{[-c|--channels]}} {{1..8}}`

- آزمودن بلندگوهای پیش‌فرض با فایل WAV مشخص:

`speaker-test {{[-t|--test]}} wav {{[-w|--wavfile]}} {{path/to/file.wav}}`

- آزمودن بلندگوهای پیش‌فرض با موج سینوسی:

`speaker-test {{[-t|--test]}} sine {{[-f|--frequency]}} {{frequency}}`
