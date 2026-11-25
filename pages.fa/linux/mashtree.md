# mashtree

> ساخت سریع درخت از ژنوم‌ها.
> درخت فیلوژنتیکی تولید نمی‌کند.
> اطلاعات بیشتر: <https://github.com/lskatz/mashtree#usage>.

- ایجاد درخت از فایل‌های fastq یا fasta با سریع‌ترین روش و چند رشته و هدایت خروجی به فایل newick:

`mashtree --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} >{{mashtree.dnd}}`

- ایجاد درخت از فایل‌های fastq یا fasta با دقیق‌ترین روش و چند رشته و هدایت خروجی به فایل newick:

`mashtree --mindepth {{0}} --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} >{{mashtree.dnd}}`

- ایجاد درخت با مقادیر اطمینان با دقیق‌ترین روش (توجه کنید گزینه‌های خود `mashtree` باید در سمت راست `--` باشند):

`mashtree_bootstrap.pl --reps {{100}} --numcpus {{12}} {{*.fastq.gz}} -- --min-depth {{0}} >{{mashtree.bootstrap.dnd}}`
