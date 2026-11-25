# blastn

> ابزار BLAST برای مقایسهٔ توالی‌های نوکلئوتیدی با یکدیگر.
> اطلاعات بیشتر: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastn_application_options/>.

- هم‌ترازسازی دو یا چند توالی با megablast (پیش‌فرض)، آستانهٔ مقدار E برابر با 1e-9 و قالب خروجی دوتایی (پیش‌فرض):

`blastn -query {{query.fa}} -subject {{subject.fa}} -evalue 1e-9`

- هم‌ترازسازی دو یا چند توالی با blastn:

`blastn -task blastn -query {{query.fa}} -subject {{subject.fa}}`

- هم‌ترازسازی دو یا چند توالی با قالب خروجی جدولی دلخواه و ذخیرهٔ خروجی در فایل:

`blastn -query {{query.fa}} -subject {{subject.fa}} -outfmt '{{6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident}}' -out {{output.tsv}}`

- جست‌وجوی پایگاه‌های دادهٔ نوکلئوتیدی با یک پرس‌وجوی نوکلئوتیدی، استفاده از ۱۶ ریسه در جست‌وجوی BLAST و نگه داشتن حداکثر ۱۰ توالی هم‌ترازشده:

`blastn -query {{query.fa}} -db {{path/to/blast_db}} -num_threads 16 -max_target_seqs 10`

- جست‌وجوی پایگاه دادهٔ نوکلئوتیدی غیرتکراری راه دور با یک پرس‌وجوی نوکلئوتیدی:

`blastn -query {{query.fa}} -db {{nt}} -remote`

- نمایش راهنما (برای راهنمای مفصل از `-help` استفاده کنید):

`blastn -h`
