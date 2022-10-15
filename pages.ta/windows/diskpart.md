# diskpart

> வட்டு, தொகுதி மற்றும் பகிர்வு மேலாளர்.
> மேலும் தகவல்: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- diskpart ஐ அதன் கட்டளை வரியை உள்ளிட நிர்வாக கட்டளை வரியில் தானாகவே இயக்கவும்:

`diskpart`

- அனைத்து வட்டுகளையும் பட்டியலிடுங்கள்:

`list disk`

- ஒரு தொகுதியைத் தேர்ந்தெடுக்கவும்:

`select volume {{volume}}`

- தேர்ந்தெடுக்கப்பட்ட தொகுதிக்கு ஒரு இயக்கி கடிதத்தை ஒதுக்கவும்:

`assign letter {{letter}}`

- ஒரு புதிய பகிர்வை உருவாக்கவும்:

`create partition primary`

- தேர்ந்தெடுக்கப்பட்ட தொகுதியை செயல்படுத்தவும்:

`active`

- வட்டு பகுதி வெளியேறு:

`exit`
