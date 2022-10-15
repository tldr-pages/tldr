# doskey

> மேக்ரோக்கள், விண்டோஸ் கட்டளைகள் மற்றும் கட்டளை வரிகளை நிர்வகிக்கவும்.
> மேலும் தகவல்: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- கிடைக்கக்கூடிய மேக்ரோக்களை பட்டியலிடுங்கள்:

`doskey /macros`

- புதிய மேக்ரோவை உருவாக்கவும்:

`doskey {{name}} = "{{command}}"`

- ஒரு குறிப்பிட்ட இயங்கக்கூடிய ஒரு புதிய மேக்ரோவை உருவாக்கவும்:

`doskey /exename={{executable}} {{name}} = "{{command}}"`

- ஒரு மேக்ரோவை அகற்று:

`doskey {{name}} =`

- நினைவகத்தில் சேமிக்கப்பட்ட அனைத்து கட்டளைகளையும் காண்பி:

`doskey /history`

- பெயர்வுத்திறனுக்காக மேக்ரோக்களை ஒரு கோப்பில் சேமிக்கவும்:

`doskey /macros > {{macinit}}`

- ஒரு கோப்பிலிருந்து மேக்ரோக்களை ஏற்றவும்:

`doskey /macrofile = {{macinit}}`