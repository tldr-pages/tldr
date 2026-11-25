# whiptail

> نمایش جعبه‌های گفت‌وگوی متنی از اسکریپت‌های پوسته.
> همچنین ببینید: `dialog`, `gum`.
> اطلاعات بیشتر: <https://manned.org/whiptail>.

- نمایش پیام ساده:

`whiptail --title "{{title}}" --msgbox "{{message}}" {{height_in_chars}} {{width_in_chars}}`

- نمایش انتخاب بله یا خیر و بازگرداندن نتیجه از طریق کد خروج:

`whiptail --title "{{title}}" --yesno "{{message}}" {{height_in_chars}} {{width_in_chars}}`

- سفارشی‌سازی متن دکمه‌های بله و خیر:

`whiptail --title "{{title}}" --yes-button "{{text}}" --no-button "{{text}}" --yesno "{{message}}" {{height_in_chars}} {{width_in_chars}}`

- نمایش جعبهٔ ورود متن:

`{{result_variable_name}}="$(whiptail --title "{{title}}" --inputbox "{{message}}" {{height_in_chars}} {{width_in_chars}} {{default_text}} 3>&1 1>&2 2>&3)"`

- نمایش جعبهٔ ورود رمز عبور:

`{{result_variable_name}}="$(whiptail --title "{{title}}" --passwordbox "{{message}}" {{height_in_chars}} {{width_in_chars}} 3>&1 1>&2 2>&3)"`

- نمایش منوی چندگزینه‌ای:

`{{result_variable_name}}=$(whiptail --title "{{title}}" --menu "{{message}}" {{height_in_chars}} {{width_in_chars}} {{menu_display_height}} {{"value_1" "display_text_1" "value_2" "display_text_2" ...}} 3>&1 1>&2 2>&3)`
