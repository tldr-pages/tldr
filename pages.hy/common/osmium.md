#օսմիում

> Բազմաֆունկցիոնալ գործիք OpenStreetMap (OSM) ֆայլերի հետ աշխատելու համար:.
> Լրացուցիչ տեղեկություններ. <https://osmcode.org/osmium-tool/manual>:.

- Ցույց տալ ֆայլի տեղեկատվությունը.:

`osmium fileinfo {{path/to/input.osm}}`

- Ցուցադրել բովանդակությունը.:

`osmium show {{path/to/input.osm}}`

- Փոխարկել ֆայլի ձևաչափը PBF-ից XML-ի.:

`osmium cat {{path/to/input.osm.pbf}} {{[-o|--output]}} {{path/to/output.osm}}`

- Աշխարհագրական շրջանը հանի՛ր տրված [b] եզրագծով.:

`osmium extract {{[-b|--bbox]}} {{min_longitude}},{{min_latitude}},{{max_longitude}},{{max_latitude}} {{path/to/input.pbf}} {{[-o|--output]}} {{path/to/output.pbf}}`

- Արտահանեք աշխարհագրական տարածաշրջան GeoJSON ֆայլով.:

`osmium extract {{[-p|--polygon]}} {{path/to/polygon.geojson}} {{path/to/input.pbf}} {{[-o|--output]}} {{path/to/output.pbf}}`

- Զտել «ռեստորան» պիտակավորված բոլոր օբյեկտները.:

`osmium tags-filter {{path/to/input.pbf}} amenity=restaurant {{[-o|--output]}} {{path/to/output.pbf}}`

- Զտիչ «ճանապարհային» օբյեկտների համար, որոնք հատկորոշված են որպես «մայրուղի»:

`osmium tags-filter {{path/to/input.pbf}} w/highway {{[-o|--output]}} {{path/to/output.pbf}}`

- Զտել «ճանապարհ» և «հարաբերություն» օբյեկտները, որոնք պիտակավորված են որպես «շենք».:

`osmium tags-filter {{path/to/input.pbf}} wr/building {{[-o|--output]}} {{path/to/output.pbf}}`
