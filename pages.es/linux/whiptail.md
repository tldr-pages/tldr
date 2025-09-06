# whiptail

> Muestra cajas de diálogo de texto para incluir en guiones de la interfaz de comando.
> Más información: <https://manned.org/whiptail>.

- Muestra un mensaje sencillo:

`whiptail --title "{{título}}" --msgbox "{{mensaje}}" {{height_in_chars}} {{width_in_chars}}`

- Muestra una opción booleana, devolviendo el resultado a través del código de salida:

`whiptail --title "{{título}}" --yesno "{{mensaje}}" {{height_in_chars}} {{width_in_chars}}`

- Personaliza el texto en los botones sí/no:

`whiptail --title "{{título}}" --yes-button "{{un texto}}" --no-button "{{otro texto}}" --yesno "{{mensaje}}" {{height_in_chars}} {{width_in_chars}}`

- Muestra una caja de entrada de texto:

`{{result_variable_name}}="$(whiptail --title "{{título}}" --inputbox "{{mensaje}}" {{height_in_chars}} {{width_in_chars}} {{texto_predeterminado}} 3>&1 1>&2 2>&3)"`

- Muestra una caja de entrada de contraseña:

`{{result_variable_name}}="$(whiptail --title "{{título}}" --passwordbox "{{mensaje}}" {{height_in_chars}} {{width_in_chars}} 3>&1 1>&2 2>&3)"`

- Muestra un menú de selección múltiple:

`{{result_variable_name}}=$(whiptail --title "{{título}}" --menu "{{mensaje}}" {{height_in_chars}} {{width_in_chars}} {{menu_display_height}} "{{valor_1}}" "{{texto_a_mostrar_1}}" "{{valor_n}}" "{{texto_a_mostrar_n}}" ..... 3>&1 1>&2 2>&3)`
