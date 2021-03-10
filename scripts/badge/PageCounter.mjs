"use strict";

import fs from 'fs';
import path from 'path';

export default async function count_pages(dir_root) {
	let result = {};
	for(let filename of (await fs.promises.readdir(dir_root))) {
		if(filename.indexOf(`pages`) == -1 || !(await fs.promises.lstat(dir_root)).isDirectory())
			continue;
		
		let code = `en`;
		if(filename !== `pages`)
			code = filename.match(/pages\.([a-zA-Z_-]+)/)[1];
		
		let dir_pages = path.join(dir_root, filename);
		
		result[code] = { count: 0 };
		for(let platform of (await fs.promises.readdir(dir_pages))) {
			result[code].count += (await fs.promises.readdir(path.join(dir_pages, platform))).length;
		}
	}
	for(let code in result) {
		result[code].percent = result[code].count / result.en.count;
	}
	return result;
}
