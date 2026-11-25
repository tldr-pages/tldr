# obabel

> تبدیل داده‌های مربوط به شیمی.
> اطلاعات بیشتر: <https://open-babel.readthedocs.io/en/latest/Command-line_tools/babel.html>.

- تبدیل فایل `.mol` به مختصات XYZ:

`obabel {{path/to/file.mol}} -O {{path/to/output_file.xyz}}`

- تبدیل رشتهٔ Simplified Molecular Input Line Entry System به تصویر ۵۰۰ در ۵۰۰:

`obabel -:"{{smiles_string}}" -O {{path/to/output_file.png}} -xp 500`

- تبدیل فایل رشته‌های SMILES به فایل‌های سه‌بعدی `.mol` جداگانه:

`obabel {{path/to/file.smi}} -O {{path/to/output_file.mol}} --gen3D -m`

- رندر کردن چند ورودی در یک تصویر:

`obabel {{path/to/file1 path/to/file2 ...}} -O {{path/to/output_file.png}}`
