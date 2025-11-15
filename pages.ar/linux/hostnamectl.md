# hostnamectl

> الحصول على اسم المضيف أو تعيينه لجهاز الكمبيوتر.
> لمزيد من التفاصيل: <https://www.freedesktop.org/software/systemd/man/hostnamectl.html>.

- الحصول على اسم المضيف لجهاز الكمبيوتر:

`hostnamectl`

- تعيين اسم المضيف لجهاز الكمبيوتر:

`sudo hostnamectl set-hostname "{{hostname}}"`

- تعيين اسم مضيف مُنَظَّم لجهاز الكمبيوتر:

`sudo hostnamectl set-hostname --static "{{hostname.example.com}}" && sudo hostnamectl set-hostname --pretty "{{hostname}}"`

- إعادة تعيين اسم المضيف إلى قيمته الافتراضية:

`sudo hostnamectl set-hostname --pretty ""`
