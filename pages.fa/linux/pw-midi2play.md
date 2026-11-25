# pw-midi2play

> پخش کلیپ‌های MIDI 2.0 از طریق PipeWire.
> توجه: این دستور نام مستعار `pw-cat --playback --midi-clip` است.
> همچنین ببینید: `pw-cat`, `pw-midi2record`, `pw-midiplay`.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- پخش فایل کلیپ MIDI 2.0 روی مقصد پیش‌فرض:

`pw-midi2play {{path/to/file.mid}}`

- پخش کلیپ MIDI با اجبار قالب MIDI مورد استفاده (پیش‌فرض `ump`):

`pw-midi2play {{[-M|--force-midi]}} {{midi|ump}} {{path/to/file.mid}}`

- نمایش راهنما:

`pw-midi2play {{[-h|--help]}}`
