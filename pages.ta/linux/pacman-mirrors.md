# pacman-mirrors

> மஞ்சாரோ லினக்ஸுக்கு பேக்மேன் கண்ணாடி பட்டியலை உருவாக்கவும்.
> பேக்மேன்-கண்ணாடிகள் ஒவ்வொரு ஓட்டத்திற்கும் உங்கள் தரவுத்தளத்தை ஒத்திசைக்க மற்றும் `sudo pacman -Syyu` ஐப் பயன்படுத்தி உங்கள் கணினியைப் புதுப்பிக்க வேண்டும்.
> மேலும் விவரத்திற்கு: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- இயல்புநிலை அமைப்புகளைப் பயன்படுத்தி ஒரு கண்ணாடி பட்டியலை உருவாக்கவும்:

`sudo pacman-mirrors --fasttrack`

- தற்போதைய கண்ணாடிகளின் நிலையைப் பெறுங்கள்:

`pacman-mirrors --status`

- தற்போதைய கிளையைக் காட்டு:

`pacman-mirrors --get-branch`

- வேறு கிளைக்கு மாறவும்:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- உங்கள் நாட்டில் உள்ள கண்ணாடிகளை மட்டும் பயன்படுத்தி, கண்ணாடி பட்டியலை உருவாக்கவும்:

`sudo pacman-mirrors --geoip`
