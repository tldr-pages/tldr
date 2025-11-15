# tar

> أداة أرشفة.
> غالبًا ما تُستخدم مع طريقة ضغط، مثل `gzip` أو `bzip2`.
> لمزيد من التفاصيل: <https://www.gnu.org/software/tar/manual/tar.html>.

- إنشاء أرشيف وكتابته إلى ملف:

`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`

- إنشاء أرشيف وكتابته إلى ملف (gzipped):

`tar czf {{path/to/target.tar.gz}} {{path/to/file1 path/to/file2 ...}}`

- إنشاء أرشيف مضغوط من مجلد باستخدام المسارات النسبية:

`tar czf {{path/to/target.tar.gz}} {{[-C|--directory]}} {{path/to/directory}} .`

- فك ضغط ملف أرشيف مضغوط في المجلد الحالي:

`tar xvf {{path/to/source.tar[.gz|.bz2|.xz]}}`

- فك ضغط ملف أرشيف مضغوط في مجلد محدد:

`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}} {{[-C|--directory]}} {{path/to/directory}}`

- إنشاء أرشيف مضغوط وكتابته إلى ملف، مع تحديد خوارزمية الضغط تلقائيًا بناءً على امتداد الملف:

`tar caf {{path/to/target.tar.xz}} {{path/to/file1 path/to/file2 ...}}`

- عرض محتويات ملف بالتفصيل:

`tar tvf {{path/to/source.tar}}`

- فك ضغط الملفات المطابقة لنمط معين من ملف أرشيف:

`tar xf {{path/to/source.tar}} --wildcards "{{*.html}}"`
