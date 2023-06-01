# cat

> फ़ाइलों को प्रिंट और जोड़ता है.
> अधिक जानकारी: <https://www.gnu.org/software/coreutils/cat>.

- फ़ाइल की सामग्री को मानक (standard) आउटपुट पर प्रिंट करें:

`cat {{path/to/file}}`

- एक आउटपुट फ़ाइल में कई फ़ाइलों को सम्‍मिलित करें:

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- आउटपुट फ़ाइल में कई फ़ाइलें जोड़ें:

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- फ़ाइल की सामग्री को अनबफर्ड ([u]nbuffered) मोड में आउटपुट फ़ाइल में कॉपी करें:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- फ़ाइल में `stdin` लिखें:

`cat - > {{path/to/file}}`

- संख्या ([n]umber) सभी आउटपुट लाइनें:

`cat -n {{path/to/file}}`

- गैर-मुद्रण योग्य और खाली स्थान वाले वर्ण प्रदर्शित करें (`M-` उपसर्ग के साथ यदि गैर-ASCII है):

`cat -v -t -e {{path/to/file}}`
