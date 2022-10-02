# compare

> 2 छवियों के बीच अंतर देखें।
> अधिक जानकारी: <https://imagemagick.org/script/compare.php>।

- 2 छवियों की तुलना करें:

`compare {{image1.png}} {{image2.png}} {{diff.png}}`

- कस्टम मीट्रिक का उपयोग करके 2 छवियों की तुलना करें:

`compare -verbose -metric {{PSNR}} {{image1.png}} {{image2.png}} {{diff.png}}`
