# am

> مدیر فعالیت های اندروید
> اطلاعات بیشتر: <https://developer.android.com/studio/command-line/adb#am>.

- یک فعالیت خاص رو شروع کن :

`am start -n {{com.android.settings/.Settings}}`

- یک فعالیت خاص رو شروع کن و داده به آن ارسال کن :

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- فعالیتی که با دسته بندی و عمل خاصی مطابقت داره رو شروع کن :

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- یک اینتنت رو به یک URI تبدیل میکنه :

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
