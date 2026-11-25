# mopac

> MOPAC (بستهٔ اوربیتال مولکولی) برنامه‌ای در شیمی کوانتومی نیمه‌تجربی بر اساس تقریب NDDO دیوار و تیل است.
> اطلاعات بیشتر: <https://github.com/openmopac/mopac>.

- انجام محاسبات مطابق فایل ورودی (`.mop`، `.dat` و `.arc`):

`mopac {{path/to/input_file}}`

- اجرای یک مثال کاری حداقلی با HF که در دایرکتوری فعلی می‌نویسد و فایل خروجی را به‌صورت جریانی نمایش می‌دهد:

`touch test.out; echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" >test.mop; mopac test.mop & tail {{[-f|--follow]}} test.out`
