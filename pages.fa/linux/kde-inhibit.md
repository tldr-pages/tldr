# kde-inhibit

> جلوگیری از عملکردهای مختلف دسکتاپ هنگام اجرای دستور.
> اطلاعات بیشتر: <https://invent.kde.org/plasma/kde-cli-tools/-/blob/master/kdeinhibit/main.cpp>.

- جلوگیری از مدیریت توان:

`kde-inhibit --power {{command}} {{command_arguments}}`

- جلوگیری از محافظ صفحه:

`kde-inhibit --screenSaver {{command}} {{command_arguments}}`

- اجرای VLC و جلوگیری از تصحیح رنگ (حالت شب) هنگام اجرای آن:

`kde-inhibit --colorCorrect {{vlc}}`
