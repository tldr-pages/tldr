# exif

> نمایش و تغییر اطلاعات EXIF در فایل‌های JPEG.
> اطلاعات بیشتر: <https://manned.org/exif>.

- نمایش همهٔ اطلاعات شناخته‌شدهٔ EXIF در یک تصویر:

`exif {{path/to/image.jpg}}`

- نمایش جدول برچسب‌های شناخته‌شدهٔ EXIF و وجود یا عدم وجود هر یک در تصویر:

`exif {{[-l|--list-tags]}} --no-fixup {{path/to/image.jpg}}`

- استخراج تصویر بندانگشتی در فایل جداگانه:

`exif {{[-e|--extract-thumbnail]}} {{[-o|--output]}} {{path/to/thumbnail.jpg}} {{path/to/image.jpg}}`

- نمایش محتوای خام برچسب «Model» در تصویر مشخص:

`exif --ifd {{0}} {{[-t|--tag]}} "Model" {{[-m|--machine-readable]}} {{path/to/image.jpg}}`

- تغییر مقدار برچسب «Artist» به John Smith و ذخیره در `new.jpg`:

`exif {{[-o|--output]}} {{path/to/new.jpg}} --ifd {{0}} {{[-t|--tag]}} "Artist" --set-value "John Smith" --no-fixup {{path/to/image.jpg}}`
