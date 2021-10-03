# input

> Send event codes or touchscreen gestures to an Android device.
> Envoie à un appareil Android des codes événements ou des gestes d'écran tactile.
> Cette commande peut être utilisé uniquement depuis `adb shell`.
> Plus d'informations : <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Envoie un code événement (un seul caractère) à un appareil Android :

`input keyevent {{event_code}}`

- Envoie du texte à un appareil Android (`%s` représentant les espaces) :

`input text "{{text}}"`

- Envoie un tapotement (tap) à un appareil Android :

`input tap {{x_pos}} {{y_pos}}`

- Envoie un mouvement de swipe à un appareil Android :

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Envoie un appui long à un appareil Android en utilisant un mouvement de swipe :

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duration_in_ms}}`
