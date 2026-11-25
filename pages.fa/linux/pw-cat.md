# pw-cat

> پخش و ضبط فایل‌های صوتی از طریق PipeWire.
> همچنین ببینید: `wpctl`, `pw-cli`.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- پخش فایل WAV روی مقصد پیش‌فرض:

`pw-cat {{[-p|--playback]}} {{path/to/file.wav}}`

- پخش فایل MIDI:

`pw-cat {{[-pm|--playback --midi]}} {{path/to/file.mid}}`

- پخش فایل DSD:

`pw-cat {{[-pd|--playback --dsd]}} {{path/to/file.dsf}}`

- پخش فایل صوتی فشرده با passthrough (نیازمند یکپارچگی FFmpeg):

`pw-cat {{[-po|--playback --encoded]}} {{path/to/file.ac3}}`

- پخش فایل WAV با کیفیت نمونه‌برداری مجدد مشخص (پیش‌فرض ۴):

`pw-cat {{[-p|--playback]}} {{[-q|--quality]}} {{0..15}} {{path/to/file.wav}}`

- ضبط فایل MIDI:

`pw-cat {{[-rm|--record --midi]}} {{path/to/file.mid}}`

- ضبط نمونه با سطح صدای ۱۲۵٪:

`pw-cat {{[-r|--record]}} --volume {{1.25}} {{path/to/file.wav}}`

- ضبط نمونه با نرخ نمونه‌برداری متفاوت:

`pw-cat {{[-r|--record]}} --rate {{6000}} {{path/to/file.wav}}`
