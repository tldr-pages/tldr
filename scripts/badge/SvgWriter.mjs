"use strict";

import LowLevelWriter from './LowLevelWriter.mjs';

class SvgWriter {
	constructor() {
		this.writer = null;
		
		this.path = [];
		this._font_size = 12;
		this._font_family = "sans-serif";
		this._font_weight = "normal";
	}
	
	async start(filename, width, height) {
		this.writer = await LowLevelWriter.Open(filename);
		await this.writer.write(`<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" version="1.1">`);
	}
	async end() {
		await this.writer.write(`</svg>\n`);
	}
	
	beginPath(x, y) {
		this.path = [ `M ${x} ${y}` ];
	}
	
	moveTo(x, y, relative = true) {
		this.path.push(`${relative?"m":"M"} ${x} ${y}`);
	}
	lineTo(x, y, relative = true) {
		this.path.push(`${relative?"l":"L"} ${x} ${y}`);
	}
	async stroke(colour, width = 2) {
		await this.writer.write(`\t<path d="${this.path.join(" ")}" stroke="${colour}" width="${width}" />\n`);
	}
	async fill(colour) {
		await this.writer.write(`\t<path d="${this.path.join(" ")}" fill="${colour}" />\n`)
	}
	
	font_size(size) { this._font_size = size; }
	font_family(family) { this._font_family = family; }
	font_weight(weight) { this._font_weight = weight; }
	
	async text(x, y, str, colour = "#333333") {
		await this.writer.write(`\t<text x="${x}" y="${y}" font-size="${this._font_size}" font-family="${this._font_family}" font-weight="${this._font_weight}" fill="${colour}">${str}</text>\n`);
	}
	
	async fillRect(x, y, width, height, colour) {
		await this.writer.write(`\t<rect x="${x}" y="${y}" width="${width}" height="${height}" fill="${colour}" />`);
	}
}

export default SvgWriter;
