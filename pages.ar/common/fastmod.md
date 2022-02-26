# fastmod

> أداة للاستبدال الجزئي للنصوص في قاعدة الأكواد لديك.
> التعبيرات الاعتيادية تعالجها : <https://crates.io/crates/regex>.
> لمزيد من العلومات: <https://github.com/facebookincubator/fastmod>.

- استبدال بالتعبيرات الاعتيادية مع تحديد المكان الذي يُستبدل فيه:

`fastmod {{regex_pattern}} {{replacement}} -d {{dir}} --iglob {{wildcard_patterns}}`

- استبدال النص كما هو (وليس التعبيرات الاعتيادية)، في ملفات .js و.json فحسب:

`fastmod -F {{match_string}} {{replacement_string}} -e json,js`

- استبدال جميع النصوص، مباشرة دون تأكيد:

`fastmod --accept-all -F {{match_string}} {{replacement_string}}`

- استبدال جميع النصوص، مباشرة دون تأكيد، مع طباعة الملفات المُستبدل فيها:

`fastmod --accept-all --print-changed-files -F {{match_string}} {{replacement_string}}`
