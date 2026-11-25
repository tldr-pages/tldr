# mkvpropedit

> تغییر ویژگی‌های فایل‌های Matroska موجود بدون remux کامل.
> اطلاعات بیشتر: <https://mkvtoolnix.download/doc/mkvpropedit.html>.

- حذف عنوان:

`mkvpropedit {{[-d|--delete]}} title {{path/to/file.mkv}}`

- علامت‌گذاری ترک زیرنویس ۳ به‌عنوان SDH، زیرنویس ویژهٔ ناشنوایان و کم‌شنوایان:

`mkvpropedit {{path/to/file.mkv}} {{[-e|--edit]}} track:s3 {{[-s|--set]}} flag-hearing-impaired=1`

- علامت‌گذاری ترک صوتی ۲ به‌عنوان پیش‌فرض:

`mkvpropedit {{path/to/file.mkv}} {{[-e|--edit]}} track:a2 {{[-s|--set]}} flag-default=1`

- حذف نام ترک ویدئویی ۱:

`mkvpropedit {{path/to/file.mkv}} {{[-e|--edit]}} track:v1 {{[-d|--delete]}} name`
