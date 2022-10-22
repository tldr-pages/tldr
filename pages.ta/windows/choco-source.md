# choco source

> சாக்லேட்டி மூலம் தொகுப்புகளுக்கான ஆதாரங்களை நிர்வகிக்கவும்.
> மேலும் விவரத்திற்கு: <https://chocolatey.org/docs/commands-source>.

- தற்போது கிடைக்கக்கூடிய ஆதாரங்களை பட்டியலிடுங்கள்:

`choco source list`

- புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name {{பெயர்}} --source {{url}}`

- நற்சான்றிதழ்களுடன் புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name {{பெயர்}} --source {{url}} --user {{பயனர்பெயர்}} --password {{கடவுச்சொல்}}`

- கிளையன்ட் சான்றிதழுடன் புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name {{பெயர்}} --source {{url}} --cert {{பாதை/டு/சான்றிதழ்}}`

- தொகுப்பு மூலத்தை இயக்கு:

`choco source enable --name {{பெயர்}}`

- ஒரு தொகுப்பு மூலத்தை முடக்கு:

`choco source disable --name {{பெயர்}}`

- தொகுப்பு மூலத்தை அகற்றவும்:

`choco source remove --name {{பெயர்}}`
