# Get-Content

> निर्दिष्ट स्थान पर मौजूद आइटम की सामग्री प्राप्त करें।

> ध्यान दें: यह कमांड केवल PowerShell के माध्यम से ही उपयोग की जा सकती है।

> अधिक जानकारी: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>

- किसी फ़ाइल की सामग्री प्रदर्शित करें:

`Get-Content -Path {{फ़ाइल\का\पथ}}`

- किसी फ़ाइल की पहली कुछ पंक्तियाँ प्रदर्शित करें:

`Get-Content -Path {{फ़ाइल\का\पथ}} -TotalCount {{10}}`

- फ़ाइल की सामग्री प्रदर्शित करें और `<Ctrl c>` दबाए जाने तक उसे पढ़ते रहें:

`Get-Content -Path {{फ़ाइल\का\पथ}} -Wait`
