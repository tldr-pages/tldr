# picotool

> إدارة لوحات Raspberry Pi Pico.
> لمزيد من التفاصيل: <https://github.com/raspberrypi/picotool>.

- عرض معلومات حول البرنامج المحمّل حاليًا على جهاز Pico:

`picotool info`

- تحميل ملف ثنائي (binary) على جهاز Pico:

`picotool load {{path/to/binary}}`

- تحويل ملف ELF أو BIN إلى تنسيق UF2:

`picotool uf2 convert {{path/to/elf_or_bin}} {{path/to/output}}`

- إعادة تشغيل جهاز Pico:

`picotool reboot`

- عرض جميع السجلات (registers) المعروفة:

`picotool otp list`

- عرض إصدار الأداة:

`picotool version`

- عرض المساعدة:

`picotool help`
