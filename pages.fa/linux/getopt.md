# getopt

> تحلیل آرگومان‌های خط فرمان.
> اطلاعات بیشتر: <https://manned.org/getopt>.

- تحلیل پرچم‌های اختیاری `verbose` و `version` با شکل کوتاه آن‌ها:

`getopt {{[-o|--options]}} vV {{[-l|--longoptions]}} verbose,version -- --version --verbose`

- افزودن گزینهٔ `--file` با آرگومان اجباری و شکل کوتاه `-f`:

`getopt {{[-o|--options]}} f: {{[-l|--longoptions]}} file: -- --file=somefile`

- افزودن گزینهٔ `--verbose` با آرگومان اختیاری و شکل کوتاه `-v` و ارسال پارامتر غیرگزینه‌ای `arg`:

`getopt {{[-o|--options]}} v:: {{[-l|--longoptions]}} verbose:: -- --verbose arg`

- پذیرفتن پرچم‌های `-r` و `--verbose` و گزینهٔ `--accept` با آرگومان اختیاری و افزودن گزینهٔ `--target` با آرگومان اجباری و شکل‌های کوتاه:

`getopt {{[-o|--options]}} rv::s::t: {{[-l|--longoptions]}} verbose,source::,target: -- -v --target target`
