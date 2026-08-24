# adb

> جسر تصحيح أندرويد (adb) : أداة للإتصال مع نسخة محاكي أندرويد أو مع أجهزة أندرويد المتصلة.
> بعض الأوامر الفرعية مثل الأمر `shell` لها توثيقات إستخدام خاصة بها.
> لمزيد من التفاصيل: <https://developer.android.com/tools/adb>.

- التحقق مما إذا كانت عملية خادم adb قيد التشغيل وبدء تشغيلها إن لم تكن كذلك:

`adb start-server`

- إنهاء عملية خادم adb:

`adb kill-server`

- بدء صَدَفة عن بُعد في نسخة المحاكي أو الجهاز المستهدف:

`adb shell`

- دفع تطبيق أندرويد إلى المحاكي أو الجهاز:

`adb install -r {{path/to/file}}.apk`

- نسخ ملف أو دليل من الجهاز المستهدف:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- نسخ ملف أو دليل إلى الجهاز المستهدف:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- عرض جميع الأجهزة المتصلة:

`adb devices`

- تحديد الجهاز الذي سيتم إرسال الأوامر إليه في حال وجود عدة أجهزة:

`adb -s {{device_id}} {{shell}}`
