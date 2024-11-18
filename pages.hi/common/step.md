# step

> सार्वजनिक कुंजी अवसंरचना (PKI) सिस्टम और कार्यप्रवाह बनाने, संचालित करने और स्वचालित करने के लिए एक उपयोग में आसान CLI उपकरण।
> देखें: `openssl`।
> अधिक जानकारी: <https://smallstep.com/docs/step-cli/>।

- एक प्रमाणपत्र की सामग्री का निरीक्षण करें:

`step certificate inspect {{सर्टिफिकेट.crt/का/पथ}}`

- एक रूट CA प्रमाणपत्र और एक कुंजी बनाएँ (निजी कुंजी पासवर्ड सुरक्षा को छोड़ने के लिए `--no-password --insecure` जोड़ें):

`step certificate create "{{उदाहरण Root CA}}" {{रूट-सीए.crt/का/पथ}} {{रूट-ca.key/का/पथ}} --profile root-ca`

- एक विशिष्ट होस्टनाम के लिए एक प्रमाणपत्र उत्पन्न करें और इसे रूट CA के साथ हस्ताक्षरित करें (सरलीकरण के लिए CSR उत्पन्न करना छोड़ सकते हैं):

`step certificate create {{hostname.example.com}} {{hostname.crt/का/पथ}} {{hostname.key/का/पथ}} --profile leaf --ca {{root-ca.crt/का/पथ}} --ca-key {{root-ca.key/का/पथ}}`

- एक प्रमाणपत्र श्रृंखला की पुष्टि करें:

`step certificate verify {{hostname.crt/का/पथ}} --roots {{root-ca.crt/का/पथ}} --verbose`

- PEM फ़ॉर्मेट के प्रमाणपत्र को DER में परिवर्तित करें और इसे डिस्क पर लिखें:

`step certificate format {{certificate.pem/का/पथ}} --out {{certificate.der/का/पथ}}`

- सिस्टम के डिफ़ॉल्ट ट्रस्ट स्टोर में एक रूट प्रमाणपत्र स्थापित करें या हटा दें:

`step certificate {{install|uninstall}} {{root-ca.crt/का/पथ}}`

- एक RSA/EC निजी और सार्वजनिक कुंजी जोड़ी बनाएँ (निजी कुंजी पासवर्ड सुरक्षा को छोड़ने के लिए `--no-password --insecure` जोड़ें):

`step crypto keypair {{सार्वजनिक/कुंजी/का/पथ}} {{निजी/कुंजी/का/पथ}} --kty {{RSA|EC}}`

- उप-कमांड के लिए सहायता दिखाएँ:

`step {{path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh}} --help`
