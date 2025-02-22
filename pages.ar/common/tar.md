# tar

> أداة أرشفة.
> غالبًا ما تُستخدم مع طريقة ضغط، مثل `gzip` أو `bzip2`.
> لمزيد من التفاصيل: <https://www.gnu.org/software/tar>.

- إنشاء[c] أرشيف وكتابته إلى ملف[f]:

`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`

- إنشاء[c] أرشيف g[z]ipped وكتابته إلى [f]ملف:

`tar czf {{path/to/target.tar.gz}} {{path/to/file1 path/to/file2 ...}}`

- إنشاء[c] أرشيف g[z]ipped (مضغوط) من مجلد باستخدام المسارات النسبية:

`tar czf {{path/to/target.tar.gz}} --directory={{path/to/directory}} .`

- فك[x] ضغط ملف أرشيف (مضغوط) في المجلد الحالي بالتفصيل [v]:

`tar xvf {{path/to/source.tar[.gz|.bz2|.xz]}}`

- فك[x] ضغط ملف أرشيف (مضغوط) في مجلد محدد:

`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}} --directory={{path/to/directory}}`

- إنشاء أرشيف[c] مضغوط وكتابته إلى ملف[f]، مع تحديد برنامج الضغط تلقائيًا[a] بناءً على امتداد الملف:

`tar caf {{path/to/target.tar.xz}} {{path/to/file1 path/to/file2 ...}}`

- عرض[t] محتويات ملف[f] tar بالتفصيل[v]:

`tar tvf {{path/to/source.tar}}`

- فك[x] ضغط الملفات المطابقة لنمط معين من ملف[f] أرشيف:

`tar xf {{path/to/source.tar}} --wildcards "{{*.html}}"`
