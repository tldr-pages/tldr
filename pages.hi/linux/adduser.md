# adduser

> उपयोगकर्ता जोड़ने की उपयोगिता।
> अधिक जानकारी: <https://manpages.debian.org/latest/adduser/adduser.html>.

- डिफ़ॉल्ट होम निर्देशिका के साथ एक नया उपयोगकर्ता बनाएं और उपयोगकर्ता को पासवर्ड सेट करने के लिए संकेत दें:

`adduser {{उपयोगकर्ता_नाम}}`

- होम निर्देशिका के बिना एक नया उपयोगकर्ता बनाएँ:

`adduser --no-create-home {{उपयोगकर्ता_नाम}}`

- Create a new user with a home directory at the specified path:

`adduser --home {{home/का/पथ}} {{उपयोगकर्ता_नाम}}`

- Create a new user with the specified shell set as the login shell:

`adduser --shell {{shell/का/पथ}} {{उपयोगकर्ता_नाम}}`

- Create a new user belonging to the specified group:

`adduser --ingroup {{group}} {{उपयोगकर्ता_नाम}}`
