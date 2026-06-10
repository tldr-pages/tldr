# ppmtoarbtxt

> Փոխակերպեք PPM պատկերը կամայական տեքստի ձևաչափի՝ ըստ ձևանմուշի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtoarbtxt.html>:.

- Փոխակերպեք PPM պատկերը տեքստի, ինչպես նշված է տվյալ ձևանմուշով.:

`ppmtoarbtxt {{path/to/template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- Փոխակերպեք PPM պատկերը տեքստի, ինչպես նշված է տվյալ ձևանմուշով, ամրացրեք նշված գլխի ձևանմուշի բովանդակությունը.:

`ppmtoarbtxt {{path/to/template}} -hd {{path/to/head_template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- Փոխակերպեք PPM պատկերը տեքստի, ինչպես նշված է տվյալ ձևանմուշով, ավելացրեք նշված պոչի ձևանմուշի բովանդակությունը.:

`ppmtoarbtxt {{path/to/template}} -hd {{path/to/tail_template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- Ցուցադրման տարբերակը:

`ppmtoarbtxt {{[-v|-version]}}`
