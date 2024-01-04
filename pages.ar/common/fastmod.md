# fastmod

> أداة للاستبدال الجزئي للنصوص في قاعدة الأكواد لديك.
> التعبيرات النمطية يعالجها قفص من بضاعة رست وهو regex.
> لمزيد من التفاصيل: <https://github.com/facebookincubator/fastmod>.

- استبدال بالتعبيرات النمطية في كل ملفات المسار الحالي وأبنائه في الملفات غير المُتجاهلة بـ .ignore أو .gitignore:

`fastmod {{regex_pattern}} {{replacement}}`

- استبدال متجاهلا حالة الحرف في ملف أو في ملفات مسار:

`fastmod --ignore-case {{regex_pattern}} {{replacement}} -- {{path/to/file path/to/directory ...}}`

- استبدال بالتعبيرات النمطية مع تحديد المكان الذي يُستبدل فيه:

`fastmod {{regex}} {{replacement}} --dir {{path/to/directory}} --iglob {{'**/*.{js,json}'}}`

- استبدال بالنص مُطابقةً (وليس التعبيرات النمطية)، في ملفات امتداداتهم إما js أو json فحسب:

`fastmod --fixed-strings {{exact_string}} {{replacement}} --extensions {{json,js}}`

- استبدال بجميع النصوص مُطابقةً، مباشرة دون مِحَثِّ تأكيد (prompt):

`fastmod --accept-all --fixed-strings {{exact_string}} {{replacement}}`

- استبدال بجميع النصوص مُطابقةً، مباشرة دون تأكيد، مع طباعة الملفات المُستبدل فيها:

`fastmod --accept-all --print-changed-files --fixed-strings {{exact_string}} {{replacement}}`
