# compare

> 2 छवियों के बीच अंतर देखें।
> अधिक जानकारी: <https://imagemagick.org/script/compare.php>।

- 2 छवियों की तुलना करें:

`compare {{छवि1.png}} {{छवि2.png}} {{अंतर.png}}`

- कस्टम मीट्रिक का उपयोग करके 2 छवियों की तुलना करें:

`compare -verbose -metric {{PSNR}} {{छवि1.png}} {{छवि2.png}} {{अंतर.png}}`
