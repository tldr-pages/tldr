# montage

> Instrumentul de montaj imagini ImageMagick.
> Dale imagini într-o grilă personalizabilă.
> Mai multe informaţii: <https://imagemagick.org/script/montage.php>

- Imagini dală într-o grilă, redimensionând automat imaginile mai mari decât dimensiunea celulei de grilă:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} montage.jpg`

- Imagini dală într-o grilă, calculând automat dimensiunea celulelor grilei din cea mai mare imagine:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 montage.jpg`

- Setați dimensiunea celulei de grilă și redimensionați imaginile pentru a se potrivi înainte de tigla:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry 640x480+0+0 montage.jpg`

- Limitați numărul de rânduri și coloane din grilă, determinând ca imaginile de intrare să se revărsă în mai multe montaje de ieșire:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 -tile 2x3 montage_%d.jpg`

- Redimensionarea și decuparea imaginilor pentru a umple complet celulele grilei înainte de placare:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 -resize 640x480^ -gravity center -crop 640x480+0+0 montage.jpg`
