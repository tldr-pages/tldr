# tr

> ترجمة الأحرف: تنفيذ عمليات الاستبدال بناءً على أحرف مفردة ومجموعات أحرف.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- استبدال جميع تكرارات حرف معين في ملف وطباعة النتيجة:

`tr < {{path/to/file}} {{find_character}} {{replace_character}}`

- استبدال جميع تكرارات حرف معين من ناتج أمر آخر:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- تعيين كل حرف من المجموعة الأولى إلى الحرف المقابل في المجموعة الثانية:

`tr < {{path/to/file}} '{{abcd}}' '{{jkmn}}'`

- حذف جميع تكرارات مجموعة الأحرف المحددة من المدخلات:

`tr < {{path/to/file}} {{[-d|--delete]}} '{{input_characters}}'`

- ضغط سلسلة من الأحرف المتطابقة إلى حرف واحد:

`tr < {{path/to/file}} {{[-s|--squeeze-repeats]}} '{{input_characters}}'`

- تحويل محتويات ملف إلى أحرف كبيرة (Upper-case):

`tr < {{path/to/file}} "[:lower:]" "[:upper:]"`

- إزالة الأحرف غير القابلة للطباعة من ملف:

`tr < {{path/to/file}} {{[-cd|--complement --delete]}} "[:print:]"`
