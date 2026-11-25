# compseq

> محاسبهٔ ترکیب واژه‌های منحصربه‌فرد در توالی‌ها.
> اطلاعات بیشتر: <https://www.bioinformatics.nl/cgi-bin/emboss/help/compseq/>.

- شمارش فراوانی مشاهده‌شدهٔ واژه‌ها در فایل FASTA با دریافت تعاملی مقادیر پارامتر:

`compseq {{path/to/file.fasta}}`

- شمارش فراوانی مشاهده‌شدهٔ جفت‌های آمینواسید از فایل FASTA و ذخیرهٔ خروجی در یک فایل متنی:

`compseq {{path/to/input_protein.fasta}} -word 2 {{path/to/output_file.comp}}`

- شمارش فراوانی مشاهده‌شدهٔ شش‌نوکلئوتیدی‌ها از فایل FASTA، ذخیرهٔ خروجی در فایل متنی و نادیده گرفتن شمارش‌های صفر:

`compseq {{path/to/input_dna.fasta}} -word 6 {{path/to/output_file.comp}} -nozero`

- شمارش فراوانی مشاهده‌شدهٔ کدون‌ها در چارچوب خوانش مشخص و نادیده گرفتن شمارش‌های هم‌پوشان (حرکت پنجره به اندازهٔ طول واژه یعنی ۳):

`compseq -sequence {{path/to/input_rna.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -frame {{1}}`

- شمارش فراوانی مشاهده‌شدهٔ کدون‌ها با جابه‌جایی چارچوب به اندازهٔ ۳ جایگاه و نادیده گرفتن شمارش‌های هم‌پوشان (باید همهٔ کدون‌ها به‌جز اولی گزارش شوند):

`compseq -sequence {{path/to/input_rna.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -frame 3`

- شمارش سه‌تایی‌های آمینواسید در فایل FASTA و مقایسه با اجرای قبلی `compseq` برای محاسبهٔ فراوانی مورد انتظار و نرمال‌شده:

`compseq -sequence {{path/to/human_proteome.fasta}} -word 3 {{path/to/output_file1.comp}} -nozero -infile {{path/to/output_file2.comp}}`

- تقریب دستور بالا بدون فایل ازپیش‌آماده‌شده با محاسبهٔ فراوانی مورد انتظار از فراوانی تک‌پایه یا تک‌باقی‌مانده در توالی‌های ورودی:

`compseq -sequence {{path/to/human_proteome.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -calcfreq`

- نمایش راهنما (برای اطلاعات بیشتر دربارهٔ گزینه‌های مرتبط و عمومی از `-help -verbose` استفاده کنید):

`compseq -help`
