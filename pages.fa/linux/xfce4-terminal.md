# xfce4-terminal

> شبیه‌ساز ترمینال XFCE4.
> اطلاعات بیشتر: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- باز کردن پنجرهٔ ترمینال جدید:

`xfce4-terminal`

- تنظیم عنوان اولیه:

`xfce4-terminal --initial-title "{{initial_title}}"`

- باز کردن زبانهٔ جدید در پنجرهٔ ترمینال فعلی:

`xfce4-terminal --tab`

- اجرای دستور در پنجرهٔ ترمینال جدید:

`xfce4-terminal --command "{{command_with_args}}"`

- باز نگه داشتن ترمینال پس از پایان دستور اجراشده:

`xfce4-terminal --command "{{command_with_args}}" --hold`

- باز کردن چند زبانهٔ جدید و اجرای دستور در هر یک:

`xfce4-terminal --tab --command "{{command1}}" --tab --command "{{command2}}"`
