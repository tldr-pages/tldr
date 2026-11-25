# blastp

> ابزار BLAST برای مقایسهٔ توالی‌های پروتئینی با یکدیگر.
> اطلاعات بیشتر: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastp_application_options/>.

- هم‌ترازسازی دو یا چند توالی با blastp، آستانهٔ مقدار E برابر با 1e-9، قالب خروجی دوتایی و نمایش خروجی روی صفحه:

`blastp -query {{query.fa}} -subject {{subject.fa}} -evalue 1e-9`

- هم‌ترازسازی دو یا چند توالی با blastp-fast:

`blastp -task blastp-fast -query {{query.fa}} -subject {{subject.fa}}`

- هم‌ترازسازی دو یا چند توالی با قالب خروجی جدولی دلخواه و ذخیرهٔ خروجی در فایل:

`blastp -query {{query.fa}} -subject {{subject.fa}} -outfmt '{{6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident}}' -out {{output.tsv}}`

- جست‌وجوی پایگاه‌های دادهٔ پروتئینی با یک پرس‌وجوی پروتئینی، استفاده از ۱۶ ریسه در جست‌وجوی BLAST و نگه داشتن حداکثر ۱۰ توالی هم‌ترازشده:

`blastp -query {{query.fa}} -db {{blast_database_name}} -num_threads 16 -max_target_seqs 10`

- جست‌وجوی پایگاه دادهٔ پروتئینی غیرتکراری راه دور با یک پرس‌وجوی پروتئینی:

`blastp -query {{query.fa}} -db {{nr}} -remote`

- نمایش راهنما (برای راهنمای مفصل از `-help` استفاده کنید):

`blastp -h`
