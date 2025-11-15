# newsboat

> هو قارئ خلاصة آر إس إس للطرفية أو الكونسول.
> لمزيد من التفاصيل: <https://newsboat.org/releases/2.40/docs/newsboat.html#_first_steps>.

- إستيراد روابط الخلاصات من ملف OPML:

`newsboat {{[-i|--import-from-opml]}} {{my-feeds.xml}}`

- إضافة روابط الخلاصات يدوياً:

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- إبدأ newsboat وقم بتحديث كل الخلاصات عند بدء التشغيل:

`newsboat {{[-r|--refresh-on-start]}}`

- نفذ أمر أو عدة أوامر مفصولة بمسافات بدون الحاجة إلي فتح newsboat:

`newsboat {{[-x|--execute]}} {{reload print-unread ...}}`

- انظر إختصارات لوحة المفاتيح (الإختصارت الأكثر شيوعاً مرئية في شريط الحالة):

`<?>`
