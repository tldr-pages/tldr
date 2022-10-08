# json5

> JSON5 फाइलहरूलाई JSON मा रूपान्तरण गर्नको लागि कमाण्ड-लाइन उपकरण।
> थप जानकारी: <https://json5.org>.

- JSON5 stdin लाई JSON stdout मा रूपान्तरण गर्नुहोस्:

`echo {{input}} | json5`

- JSON5 फाइललाई JSON र आउटपुटलाई stdout मा रूपान्तरण गर्नुहोस्:

`json5 {{path/to/input_file.json5}}`

- JSON5 फाइललाई निर्दिष्ट JSON फाइलमा रूपान्तरण गर्नुहोस्:

`json5 {{path/to/input_file.json5}} --out-file {{path/to/output_file.json}}`

- JSON5 फाइल प्रमाणित गर्नुहोस्:

`json5 {{path/to/input_file.json5}} --validate`

- इन्डेन्ट द्वारा (वा ट्याबहरूको लागि "t") गर्न खाली ठाउँहरूको संख्या निर्दिष्ट गर्नुहोस्:

`json5 --space {{indent_amount}}`

- उपलब्ध विकल्पहरू हेर्नुहोस्:

`json5 --help`
