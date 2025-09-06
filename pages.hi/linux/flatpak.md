# flatpak

> फ्लैटपैक अनुप्रयोग और रनटाइम बनाएं, स्थापित करें और चलाएं।
> अधिक जानकारी: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>।

- एक स्थापित अनुप्रयोग चलाएं:

`flatpak run {{नाम}}`

- दूरस्थ स्रोत से एक अनुप्रयोग स्थापित करें:

`flatpak install {{दूरस्थ}} {{नाम}}`

- सभी स्थापित अनुप्रयोग और रनटाइम की सूची दिखाएं:

`flatpak list`

- सभी स्थापित अनुप्रयोग और रनटाइम को अद्यतित करें:

`flatpak update`

- एक दूरस्थ स्रोत जोड़ें:

`flatpak remote-add --if-not-exists {{दूरस्थ_नाम}} {{दूरस्थ_URL}}`

- एक स्थापित अनुप्रयोग हटाएं:

`flatpak remove {{नाम}}`

- सभी अउपयोग नहीं किए जा रहे अनुप्रयोग हटाएं:

`flatpak remove --unused`

- एक स्थापित अनुप्रयोग के बारे में जानकारी दिखाएं:

`flatpak info {{नाम}}`
