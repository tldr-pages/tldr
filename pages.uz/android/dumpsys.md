# dumpsys

> Android tizimi xizmatlari to'g'risida malumot berish.
> Bu buyruq faqatgina `adb shell` bilan ishlatiladi.
> Ko'proq malumot: <https://developer.android.com/tools/dumpsys>.

- Tizimning barcha xizmatlari haqida tahliliy malumot:

`dumpsys`

- Biron xizmat to'g'risida tahliliy malumot olish:

`dumpsys {{service}}`

- `dumpsys` buyrug'idagi barcha xizmatlarni chiqaradi:

`dumpsys -l`

- Xizmatning argumentlarini chiqaradi:

`dumpsys {{service}} -h`

- Tahliliy malumotlar ro'yhatidan biron xizmatni qoldirish:

`dumpsys --skip {{service}}`

- Time out ni belgilash (sekundlarda):

`dumpsys -t {{sekund}}`
