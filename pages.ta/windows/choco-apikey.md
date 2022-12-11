# choco-apikey

> சாக்லேட்டி மூலங்களுக்கான API விசைகளை நிர்வகிக்கவும்.
> மேலும் விவரத்திற்கு:  <https://chocolatey.org/docs/commands-apikey>.

- ஆதாரங்களின் பட்டியலையும் அவற்றின் API விசைகளையும் காட்டவும்:

`choco apikey`

- ஒரு குறிப்பிட்ட மூலத்தையும் அதன் API விசையையும் காண்பி:

`choco apikey --source "{{மூல_முகவரி}}"`

- மூலத்திற்கான API விசையை அமைக்கவும்:

`choco apikey --source "{{மூல_முகவரி}}" --key "{{api_key}}"`

- மூலத்திற்கான API விசையை அகற்றவும்:

`choco apikey --source "{{மூல_முகவரி}}" --remove`
