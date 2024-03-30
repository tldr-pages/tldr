# parted

> Програма для роботи з розділами.
> Дивіться також: `partprobe`.
> Більше інформації: <https://www.gnu.org/software/parted/parted.html>.

- Перелічити розділи на всіх блокових пристроях:

`sudo parted --list`

- Запустити інтерактивний режим із вибраним диском:

`sudo parted {{/dev/sdX}}`

- Створити нову таблицю розділів указаного типу міток:

`sudo parted --script {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- Показати інформацію про розділ в інтерактивному режимі:

`print`

- Вибрати диск в інтерактивному режимі:

`select {{/dev/sdX}}`

- Створити розділ на 16 ГБ із зазначеною файловою системою в інтерактивному режимі:

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- Змінити розмір розділу в інтерактивному режимі:

`resizepart {{/dev/sdXN}} {{кінцева_позиція_розділу}}`

- Видалити розділ в інтерактивному режимі:

`rm {{/dev/sdXN}}`
