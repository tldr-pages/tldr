# fcrackzip

> ابزار شکستن رمز عبور بایگانی ZIP.
> اطلاعات بیشتر: <https://manned.org/fcrackzip>.

- جست‌وجوی فراگیر رمز عبور با طول ۴ تا ۸ نویسه و فقط شامل حروف و اعداد (ترتیب مهم است):

`fcrackzip {{[-b|--brute-force]}} {{[-l|--length]}} 4-8 {{[-c|--charset]}} aA1 {{archive}}`

- جست‌وجوی فراگیر رمز عبور ۳ نویسه‌ای در حالت مفصل که فقط شامل حروف کوچک، `$` و `%` است:

`fcrackzip {{[-v|--verbose]}} {{[-b|--brute-force]}} {{[-l|--length]}} 3 {{[-c|--charset]}} a:$% {{archive}}`

- جست‌وجوی فراگیر رمز عبوری که فقط شامل حروف کوچک و نویسه‌های ویژه است:

`fcrackzip {{[-b|--brute-force]}} {{[-l|--length]}} 4 {{[-c|--charset]}} a! {{archive}}`

- جست‌وجوی فراگیر رمز عبور فقط شامل رقم، با شروع از رمز `12345`:

`fcrackzip {{[-b|--brute-force]}} {{[-l|--length]}} 5 {{[-c|--charset]}} 1 {{[-p|--init-password]}} 12345 {{archive}}`

- شکستن رمز عبور با فهرست واژه‌ها:

`fcrackzip {{[-u|--use-unzip]}} {{[-D|--dictionary]}} {{[-p|--init-password]}} {{wordlist}} {{archive}}`

- ارزیابی عملکرد شکستن رمز:

`fcrackzip {{[-B|--benchmark]}}`
