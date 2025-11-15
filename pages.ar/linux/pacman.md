# pacman

> أداة مدير الحزم لنظام Arch Linux.
> انظر أيضًا: `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
> لأوامر مكافئة في مديري الحزم الآخرين، انظر <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> لمزيد من التفاصيل: <https://manned.org/pacman.8>.

- مزامنة وتحديث جميع الحزم:

`sudo pacman -Syu`

- تثبيت حزمة جديدة:

`sudo pacman -S {{package}}`

- إزالة حزمة والتبعيات الخاصة بها:

`sudo pacman -Rs {{package}}`

- البحث في قاعدة بيانات الحزم عن تعبير نمطي (Regular Expresssion) أو كلمة مفتاحية:

`pacman -Ss "{{search_pattern}}"`

- البحث في قاعدة البيانات عن الحزم التي تحتوي على ملف محدد:

`pacman -F "{{file_name}}"`

- عرض الحزم المثبتة بشكل صريح (تم تثبيتها يدويًا بواسطة المستخدم) مع إصداراتها:

`pacman -Qe`

- عرض الحزم اليتيمة (المثبتة كـ تبعيات ولكنها غير مطلوبة من قبل أي حزمة):

`pacman -Qtdq`

- تفريغ ذاكرة التخزين المؤقت بالكامل لـ `pacman`:

`sudo pacman -Scc`
