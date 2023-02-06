# whiptail

> Szövegalapú párbeszédpanelek megjelenítése shell szkriptekből. További információ: <https://manned.org/whiptail>.

- Egyszerű üzenet megjelenítése:

`whiptail --title "{{title}}" --msgbox "{{message}}" {{height_in_chars}} {{width_in_chars}}`

- Boolean választás megjelenítése, az eredmény visszaadása a kilépési kódon keresztül:

`whiptail --title "{{title}}" --yesno "{{message}}" {{height_in_chars}} {{width_in_chars}}`

- Az igen/nem gombok szövegének testreszabása:

`whiptail --title "{{title}}" --yes-button "{{text}}" --no-button "{{text}}" --yesno "{{message}}" {{height_in_chars}} {{width_in_chars}}`

- Szöveges beviteli mező megjelenítése:

`{{result_variable_name}}="$(whiptail --title "{{title}}" --inputbox "{{message}}" {{height_in_chars}} {{width_in_chars}} {{default_text}} 3>&1 1>&2 2>&3)"`

- Jelszó beviteli mező megjelenítése:

`{{result_variable_name}}="$(whiptail --title "{{title}}" --passwordbox "{{message}}" {{height_in_chars}} {{width_in_chars}} 3>&1 1>&2 2>&3)"`

- Többválasztós menü megjelenítése:

`{{result_variable_name}}=$(whiptail --title "{{title}}" --menu "{{message}}" {{height_in_chars}} {{width_in_chars}} {{menu_display_height}} "{{value_1}}" "{{display_text_1}}" "{{value_n}}" "{{display_text_n}}" ..... 3>&1 1>&2 2>&3)`
