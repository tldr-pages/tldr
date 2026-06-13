# PSVersionTable

> वर्तमान PowerShell संस्करण प्राप्त करने के लिए एक केवल-पढ़ने योग्य चर (जैसे `$PSVersionTable`)।
> यह कमांड केवल PowerShell के तहत चलाया जा सकता है।
> अधिक जानकारी: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables#psversiontable>।

- वर्तमान में स्थापित PowerShell संस्करण और संस्करण का एक सारांश प्रिंट करें:

`$PSVersionTable`

- PowerShell का विस्तृत (मुख्य, उप, निर्माण, और संशोधन) संस्करण संख्या प्राप्त करें:

`$PSVersionTable.PSVersion`

- सभी समर्थित PowerShell स्क्रिप्ट संस्करणों की सूची बनाएं जिन्हें यह PowerShell संस्करण समर्थन करता है:

`$PSVersionTable.PSCompatibleVersions`

- नवीनतम Git कमिट ID प्राप्त करें जिस पर वर्तमान में स्थापित PowerShell संस्करण आधारित है (PowerShell 6.0 और बाद के संस्करण पर कार्य करता है):

`$PSVersionTable.GitCommitId`

- जांचें कि क्या उपयोगकर्ता PowerShell Core (6.0 या बाद के संस्करण) चला रहा है या मूल "Windows PowerShell" (संस्करण 5.1 या उससे नीचे):

`$PSVersionTable.PSEdition`
