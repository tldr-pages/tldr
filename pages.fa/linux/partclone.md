# partclone

> کپی و بازیابی پارتیشن‌ها به تصویر یا از آن با صرف‌نظر از بلوک‌های خالی.
> اطلاعات بیشتر: <https://manned.org/partclone>.

- کپی پارتیشن در تصویر:

`sudo partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-c|--clone]}} {{[-s|--source]}} {{/dev/sdXY}} {{[-o|--output]}} {{path/to/backup.img}}`

- بازیابی پارتیشن از تصویر:

`sudo partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-c|--clone]}} {{[-s|--source]}} {{path/to/backup.img}} {{[-o|--output]}} {{/dev/sdXY}}`

- نمایش راهنما:

`partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-h|--help]}}`
