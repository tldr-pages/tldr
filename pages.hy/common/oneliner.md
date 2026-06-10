# oneliner

> Պարզ անգլերենը վերածեք կեղևի հրամանների՝ օգտագործելով OpenAI, Claude կամ տեղական LLM-ները, որոնք նախատեսված են ուսուցանելու, այլ ոչ թե փոխարինելու ձեր գիտելիքները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/dorochadev/oneliner#-usage-flags>:.

- Ստեղծեք կեղևի հրաման պարզ անգլերենից.:

`oneliner "{{find all jpg files larger than 10MB}}"`

- Բացատրեք, թե ինչ է անում հրամանը.:

`oneliner {{[-e|--explain]}} "{{delete node_modules recursively}}"`

- Պատճենեք ստեղծված հրամանը clipboard-ում.:

`oneliner {{[-c|--clipboard]}} "{{compress all pdfs}}"`

- Ցուցադրել հրամանի մանրամասն, կրթական բաժանումը.:

`oneliner {{[-b|--breakdown]}} "{{list all active network connections}}"`

- Կատարեք ստեղծված հրամանը (օգտագործեք զգուշությամբ).:

`oneliner {{[-r|--run]}} "{{list files larger than 1GB}}"`

- Ինտերակտիվ կերպով հաստատեք նախքան ստեղծված հրամանը կատարելը.:

`oneliner {{[-i|--interactive]}} "{{delete temporary files in /tmp}}"`
