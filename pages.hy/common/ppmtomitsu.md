# ppmtomitsu

> Փոխարկել PPM պատկերը Mitsubishi S340-10 ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtomitsu.html>:.

- Փոխարկել PPM պատկերը MITSU ֆայլի.:

`ppmtomitsu {{path/to/file.ppm}} > {{path/to/file.mitsu}}`

- Մեծացրեք պատկերը նշված գործակցով, օգտագործեք նշված հստակությունը և արտադրեք `n` պատճեններ.:

`ppmtomitsu {{[-e|-enlarge]}} {{1|2|3}} {{[-s|-sharpness]}} {{1|2|3|4}} {{[-c|-copy]}} {{n}} {{path/to/file.ppm}} > {{path/to/file.mitsu}}`

- Տպագրության գործընթացում օգտագործեք տվյալ միջավայրը.:

`ppmtomitsu {{[-m|-media]}} {{A|A4|AS|A4S}} {{path/to/file.ppm}} > {{path/to/file.mitsu}}`
