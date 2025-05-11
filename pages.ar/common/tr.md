# tr

> ترجمة الأحرف: تنفيذ عمليات الاستبدال بناءً على أحرف مفردة ومجموعات أحرف.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- استبدال جميع تكرارات حرف معين في ملف وطباعة النتيجة:

`tr {{find_character}} {{replace_character}} < {{path/to/file}}`

- استبدال جميع تكرارات حرف معين من ناتج أمر آخر:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- تعيين كل حرف من المجموعة الأولى إلى الحرف المقابل في المجموعة الثانية:

`tr '{{abcd}}' '{{jkmn}}' < {{path/to/file}}`

- حذف جميع تكرارات مجموعة الأحرف المحددة من المدخلات:

`tr {{[-d|--delete]}} '{{input_characters}}' < {{path/to/file}}`

- ضغط سلسلة من الأحرف المتطابقة إلى حرف واحد:

`tr {{[-s|--squeeze-repeats]}} '{{input_characters}}' < {{path/to/file}}`

- تحويل محتويات ملف إلى أحرف كبيرة (Upper-case):

`tr "[:lower:]" "[:upper:]" < {{path/to/file}}`

- إزالة الأحرف غير القابلة للطباعة من ملف:

`tr {{[-cd|--complement --delete]}} "[:print:]" < {{path/to/file}}`
