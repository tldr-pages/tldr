# fastmod

> أداة للاستبدال الجزئي للنصوص في قاعدة الأكواد لديك.
> التعبيرات الاعتيادية يعالجها قفص من بضاعة رست وهو regex.
> لمزيد من العلومات: <https://github.com/facebookincubator/fastmod>.

- استبدال التعبيرات الاعتيادية في كل ملفات المسار الحالي وأبنائه في الملفات غير المُتجاهلة بـ .ignore أو .gitignore

`fastmod {{regex_pattern}} {{replacement}}`

- استبدال التعبيرات الاعتيادية مع تحديد المكان الذي يُستبدل فيه:

`fastmod {{regex}} {{replacement}} -d {{src/}} --iglob {{'**/*.{js,json}'}}`

- استبدال النص كما هو (وليس التعبيرات الاعتيادية)، في ملفات .js و.json فحسب:

`fastmod -F {{match}} {{replacement}} -e {{json,js}}`

- استبدال جميع النصوص، مباشرة دون تأكيد:

`fastmod --accept-all -F {{match}} {{replacement}}`

- استبدال جميع النصوص، مباشرة دون تأكيد، مع طباعة الملفات المُستبدل فيها:

`fastmod --accept-all --print-changed-files -F {{match}} {{replacement}}`
