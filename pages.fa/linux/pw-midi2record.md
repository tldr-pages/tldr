# pw-midi2record

> ضبط کلیپ‌های MIDI 2.0 از طریق PipeWire.
> توجه: این دستور نام مستعار `pw-cat --record --midi-clip` است.
> همچنین ببینید: `pw-cat`, `pw-midi2play`, `pw-midirecord`.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- ضبط فایل کلیپ MIDI 2.0 از منبع پیش‌فرض:

`pw-midi2record {{path/to/file.mid}}`

- ضبط کلیپ MIDI با اجبار قالب MIDI مورد استفاده (پیش‌فرض `ump`):

`pw-midi2record {{[-M|--force-midi]}} {{midi|ump}} {{path/to/file.mid}}`

- نمایش راهنما:

`pw-midi2record {{[-h|--help]}}`
