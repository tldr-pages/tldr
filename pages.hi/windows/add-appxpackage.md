# Add-AppxPackage

> उपयोगकर्ता खाते में एक हस्ताक्षरित ऐप पैकेज (`.appx`, `.msix`, `.appxbundle` और `.msixbundle`) जोड़ने के लिए एक PowerShell उपयोगिता।
> अधिक जानकारी: <https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>।

- एक ऐप पैकेज जोड़ें:

`Add-AppxPackage -Path {{पैकेज.msix\का\पथ}}`

- निर्भरता के साथ एक ऐप पैकेज जोड़ें:

`Add-AppxPackage -Path {{पैकेज.msix\का\पथ}} -DependencyPath {{निर्भरता.msix\का\पथ}}`

- ऐप इंस्टॉलर फ़ाइल का उपयोग करके एक ऐप इंस्टॉल करें:

`Add-AppxPackage -AppInstallerFile {{ऐप_इंस्टॉलर.msix\का\पथ}}`

- एक अहस्ताक्षरित पैकेज जोड़ें:

`Add-AppxPackage -Path {{पैकेज.msix\का\पथ}} -DependencyPath {{निर्भरता.msix\का\पथ}} -AllowUnsigned`
