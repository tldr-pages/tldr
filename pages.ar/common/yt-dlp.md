# yt-dlp

> تّفرع من youtube-dl مع ميزات إضافية وتحسينات.
> لتحميل الفيديوهات من Youtube ومواقع أخرى.
> أنظر أيضاً: `ytfzf`.
> لمزيد من التفاصيل: <https://github.com/yt-dlp/yt-dlp#usage-and-options>.

- لتحميل فيديو أو قائمة تشغيل (مع الأعدادات الأفتراضية):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- عرض جميع الصيغ المتوفرة للتحميل من الفيديو:

`yt-dlp {{[-F|--list-formats]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- تحميل فيديو أو قائمة تشغيل بأفضل جودة MP4 متاح (الأفتراضي: "bv\*+ba/b"):

`yt-dlp {{[-f|--format]}} "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- أستخراج الصوت فقط من الفيديو (يلزم توفر ffmpeg أو ffprobe):

`yt-dlp {{[-x|--extract-audio]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- لتحديد صيغة الصوت وجودته من الصوت المستخرج  (بين 0 (الأفضل) و 10 (الأسوء), الأفتراضي = 5):

`yt-dlp {{[-x|--extract-audio]}} --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- تحميل فقط العناصر الثانية والرابعة والخامسة والسادسة والأخيرة من قائمة التشغيل (مع العلم أنّ العنصر الأول يُحسب برقم 1، وليس 0):

`yt-dlp {{[-I|--playlist-items]}} 2,4:6,-1 "{{https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA}}"`

- تحميل كل قوائم التشغيل من قناة اليويتوب/المستخدم, مع حفظ كل قائمة تشغيل في مجلد منفصل:

`yt-dlp {{[-o|--output]}} "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- تحميل دورة من Udemy مع حفظ كل فصل في مجلد منفصل:

`yt-dlp {{[-u|--username]}} {{user}} {{[-p|--password]}} {{password}} {{[-P|--paths]}} "{{path/to/directory}}" {{[-o|--output]}} "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`
