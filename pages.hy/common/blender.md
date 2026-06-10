#բլենդեր

> Հրամանի տող ինտերֆեյս Blender 3D համակարգչային գրաֆիկայի հավելվածի համար:.
> Փաստարկները կատարվում են ըստ տրված հերթականության:.
> Լրացուցիչ տեղեկություններ. <https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>:.

- Պատկերացրեք անիմացիայի բոլոր կադրերը հետին պլանում՝ առանց միջերեսը բեռնելու (արդյունքը պահվում է `/tmp`-ում):

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-a|--render-anim]}}`

- Պատկերացրեք անիմացիա՝ օգտագործելով պատկերի անվանման հատուկ օրինաչափություն՝ `.blend` ֆայլին հարաբերական ճանապարհով (`//`):

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-o|--render-output]}} //{{render/frame_###.png}} {{[-a|--render-anim]}}`

- Պատկերացրեք անիմացիայի 10-րդ կադրը որպես մեկ պատկեր՝ պահպանված գոյություն ունեցող գրացուցակում (բացարձակ ուղի).:

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-o|--render-output]}} /{{path/to/output_directory}} {{[-f|--render-frame]}} {{10}}`

- Անիմացիայի երկրորդ վերջին կադրը ներկայացրեք որպես JPEG պատկեր՝ պահպանված գոյություն ունեցող գրացուցակում (հարաբերական ուղի).:

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-o|--render-output]}} //{{output_directory}} {{[-f|--render-frame]}} {{JPEG}} {{[-f|--render-frame]}} {{-2}}`

- Ներկայացրեք կոնկրետ տեսարանի անիմացիան՝ սկսած կադր 10-ից և ավարտվում կադրով 500:

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-S|--scene]}} {{scene_name}} {{[-s|--frame-start]}} {{10}} {{[-e|--frame-end]}} {{500}} {{[-a|--render-anim]}}`

- Պատկերացրեք անիմացիա որոշակի լուծաչափով, անցնելով Python արտահայտություն.:

`blender {{[-b|--background]}} {{path/to/file.blend}} --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' {{[-a|--render-anim]}}`

- Սկսեք ինտերակտիվ Blender նիստը տերմինալում Python կոնսոլով (գործարկելուց հետո արեք `import bpy`):

`blender {{[-b|--background]}} --python-console`
