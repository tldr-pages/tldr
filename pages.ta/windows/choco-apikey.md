# choco-apikey

> சாக்லேட் மூலங்களுக்கான API விசைகளை நிர்வகிக்கவும்.
> மேலும் தகவல்:  <https://chocolatey.org/docs/commands-apikey>.

- ஆதாரங்களின் பட்டியலையும் அவற்றின் ஏப்ஏய் விசைகளையும் காட்டவும்:

`choco apikey`

- ஒரு குறிப்பிட்ட மூலத்தையும் அதன் ஏப்ஏய் விசையையும் காண்பி:

`choco apikey --source "{{source_url}}"`

- மூலத்திற்கான ஏப்ஏய் விசையை அமைக்கவும்:

`choco apikey --source "{{source_url}}" --key "{{api_key}}"`

- மூலத்திற்கான ஏப்ஏய் விசையை அகற்றவும்:

`choco apikey --source "{{source_url}}" --remove`
