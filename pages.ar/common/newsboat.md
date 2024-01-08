# newsboat

> هو قارئ خلاصة آر إس إس للطرفية أو الكونسول.
> لمزيد من التفاصيل: <https://newsboat.org/>.

- إستيراد روابط الخلاصات من ملف OPML:

`newsboat -i {{my-feeds.xml}}`

- إضافة روابط الخلاصات يدوياً:

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- إبدأ newsboat وقم بتحديث كل الخلاصات عند بدء التشغيل:

`newsboat -r`

- نفذ أمر أو عدة أوامر مفصولة بمسافات بدون الحاجة إلي فتح newsboat:

`newsboat -x {{reload print-unread ...}}`

- انظر إختصارات لوحة المفاتيح (الإختصارت الأكثر شيوعاً مرئية في شريط الحالة):

`?`
