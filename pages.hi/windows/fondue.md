# fondue

> वैकल्पिक विंडोज़ सुविधाएँ स्थापित करें।
> अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>।

- एक विशिष्ट विंडोज़ सुविधा सक्षम करें:

`fondue /enable-feature:{{विशेषता}}`

- उपयोगकर्ता के लिए सभी आउटपुट संदेश छिपाएँ:

`fondue /enable-feature:{{विशेषता}} /hide-ux:all`

- त्रुटि रिपोर्टिंग के लिए कॉलर प्रक्रिया का नाम निर्दिष्ट करें:

`fondue /enable-feature:{{विशेषता}} /caller-name:{{नाम}}`
