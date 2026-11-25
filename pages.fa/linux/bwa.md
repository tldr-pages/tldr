# bwa

> ابزار هم‌ترازسازی Burrows-Wheeler.
> نگاشت توالی‌های کوتاه DNA با واگرایی کم به یک ژنوم مرجع بزرگ، مانند ژنوم انسان.
> اطلاعات بیشتر: <https://manned.org/bwa>.

- نمایه‌سازی ژنوم مرجع:

`bwa index {{path/to/reference.fa}}`

- نگاشت خوانش‌های تک‌انتها به ژنوم نمایه‌شده با ۳۲ ریسه با `-t` و فشرده‌سازی نتیجه برای صرفه‌جویی در فضا:

`bwa mem -t 32 {{path/to/reference.fa}} {{path/to/read_single_end.fq.gz}} | gzip >{{path/to/alignment_single_end.sam.gz}}`

- نگاشت خوانش‌های دو‌انتها به ژنوم نمایه‌شده با ۳۲ ریسه با `-t` و فشرده‌سازی نتیجه برای صرفه‌جویی در فضا:

`bwa mem -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip >{{path/to/alignment_pair_end.sam.gz}}`

- نگاشت خوانش‌های دو‌انتها به ژنوم نمایه‌شده با ۳۲ ریسه با `-t`، علامت‌گذاری تطابق‌های شکستهٔ کوتاه‌تر به‌عنوان ثانویه با `-M` برای سازگاری فایل SAM با نرم‌افزار Picard و فشرده‌سازی نتیجه:

`bwa mem -M -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip >{{path/to/alignment_pair_end.sam.gz}}`

- نگاشت خوانش‌های دو‌انتها به ژنوم نمایه‌شده با ۳۲ ریسه با `-t` و افزودن توضیحات FASTA/Q (مانند BC:Z:CGTAC) با `-C` به نتیجهٔ فشرده:

`bwa mem -C -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip >{{path/to/alignment_pair_end.sam.gz}}`
