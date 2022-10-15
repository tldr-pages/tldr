# choco source

> சாக்லேட் மூலம் தொகுப்புகளுக்கான ஆதாரங்களை நிர்வகிக்கவும்.
> மேலும் தகவல்: <https://chocolatey.org/docs/commands-source>.

- தற்போது கிடைக்கக்கூடிய ஆதாரங்களை பட்டியலிடுங்கள்:

`choco source list` 

- புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name {{name}} --source {{url}}`

- நற்சான்றிதழ்களுடன் புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name {{name}} --source {{url}} --user {{username}} --password {{password}}`

- கிளையன்ட் சான்றிதழுடன் புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name {{name}} --source {{url}} --cert {{path/to/certificate}}`

- தொகுப்பு மூலத்தை இயக்கு:

`choco source enable --name {{name}}`

- ஒரு தொகுப்பு மூலத்தை முடக்கு:

`choco source disable --name {{name}}`

- தொகுப்பு மூலத்தை அகற்றவும்:

`choco source remove --name {{name}}`