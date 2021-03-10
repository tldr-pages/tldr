#!/usr/bin/env node
"use strict";

import SvgWriter from './SvgWriter.mjs';
import count_pages from './PageCounter.mjs';

const dirpath = process.argv[2];
const filepath_output = process.argv[3];
const colours = {
	text: `#97d6d2`,
	text_percent: `#333333`,
	lines: `#4d9182`,
	bg: `#203050`,
	green: `hsl(128, 63%, 45%)`,
	yellow: `hsl(57, 81%, 54%)`,
	orange: `hsl(32, 93%, 48%)`,
	red: `hsl(10, 72%, 58%)`
}
const settings = {
	width: 150,
	divider: 64,
	font_size: 20,
	font_family: "sans-serif",
	threshold: {
		green: 0.9,
		yellow: 0.5,
		orange: 0.1
	}
};

if(typeof filepath_output !== "string") {
	console.error(`tldr translations badge maker

Usage:
	scripts/badge/index.mjs <path_to_repo_root> <path_to_output_file.svg>`);
	process.exit();
}

function get_colour_percent(percent) {
	if(percent >= settings.threshold.green)
		return colours.green;
	if(percent >= settings.threshold.yellow)
		return colours.yellow;
	if(percent >= settings.threshold.orange)
		return colours.orange;
	return colours.red;
}

function get_date() {
	let d = new Date();
	return d.toISOString().split("T")[0];
}

(async () => {
    "use strict";
    
	console.log(`>>> Counting pages [ 1 / 2 ]`);
  let pages = await count_pages(dirpath);
	console.log(`>>> complete - stats:`, pages);
	
	console.log(`>>> Writing SVG [ 2 / 2 ]`);
	let header_height = settings.font_size*2 + 10;
	let height = header_height + Object.keys(pages).length * settings.font_size + settings.font_size;
	
	let svg = new SvgWriter();
	await svg.start(
		filepath_output,
		settings.width, height
	);
	
	// Header
	// -------------------------------------------
	await svg.fillRect(0, 0, settings.width, height, colours.bg);
	svg.font_weight("bold");
	await svg.text(10, settings.font_size, "tldr-pages", colours.text);
	svg.font_weight("normal");
	await svg.text(10, settings.font_size*2, "translation progress", colours.text);
	
	// Translation stats
	// -------------------------------------------
	let y = header_height, i = 0;
	for(let code in pages) {
		let lang = pages[code];
		await svg.fillRect(
			settings.divider, y,
			settings.width - settings.divider, settings.font_size,
			get_colour_percent(lang.percent)
		);
		if(i % 2 == 0)
			await svg.fillRect(0, y, settings.width, settings.font_size, `rgba(200, 200, 200, 0.25)`);
		
		let text_y = y + settings.font_size * 0.7;
		await svg.text(10, text_y, code, colours.text);
		await svg.text(settings.divider + 10, text_y,
			`${(lang.percent * 100).toFixed(2)}%`, colours.text_percent);
		
		i++; y += settings.font_size;
	}
	
	// Footer
	// -------------------------------------------
	await svg.text(10, height - settings.font_size*0.28, `Updated ${get_date()}`, colours.text);
	
	// Dividing Lines
	// -------------------------------------------
	svg.beginPath(0, header_height);
	svg.lineTo(settings.width, 0);
	svg.moveTo(settings.divider, header_height, false);
	svg.lineTo(settings.divider, height - settings.font_size, false);
	svg.moveTo(0, height - settings.font_size, false);
	svg.lineTo(settings.width, height - settings.font_size, false);
	
	await svg.stroke(colours.lines, 4);
	
	
	await svg.end();
	console.log(`>>> complete`);
})();
