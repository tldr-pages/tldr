"use strict";

import fs from 'fs';
import { EventEmitter, once } from 'events';

/**
 * File writer class that ensures that no data will be lost.
 * Ref https://stackabuse.com/writing-to-files-in-node-js/
 * Imported from our personal massCode snippets db, and written
 * to fix the most frustrating bug in my PhD data processing code....
 * @extends EventEmitter
 */
class LowLevelWriter extends EventEmitter {
	constructor() {
		super();
		
		this.fd = null;
		this.is_writing = false;
	}
	
	open(filename) {
		return new Promise((resolve, reject) => {
			if(this.fd !== null) {
				reject("InvalidOperationError: Can't open multiple files on a single LowLevelWriter.");
				return false;
			}
			
			fs.open(filename, "w", (error, fd) => {
				if(error) reject(error);
				this.emit("open");
				this.fd = fd;
				resolve();
			});
		});
	}
	
	write(chunk) {
		return new Promise((resolve, reject) => {
			this.is_writing = true;
			this.emit("write_start");
			if(!Buffer.isBuffer(chunk))
				chunk = Buffer.from(chunk.toString(), "utf8");
			
			fs.write(this.fd, chunk, (err, bytes_written) => {
				if(err) {
					reject(err);
					return false;
				}
				if (bytes_written != chunk.length) {
					reject(`Error: Buffer has length of ${chunk.length} bytes, but ${bytes_written} bytes were actually written.`);
					return false;
				}
				
				this.is_writing = false;
				this.emit("write_end");
				resolve(bytes_written);
			});
		});
	}
	
	close() {
		return new Promise((resolve, reject) => {
			let prom = null;
			if(this.is_writing)
				prom = once(this, "write_end")
			else
				prom = Promise.resolve();
			
			prom.then(() => {
				fs.close(this.fd, (error) => {
					if(error) {
						reject(error);
						return false;
					}
					this.emit("close");
					resolve();
				});
			});
		})
	}
}

LowLevelWriter.Open = async (filename) => {
	let result = new LowLevelWriter();
	await result.open(filename);
	return result;
}

export default LowLevelWriter;
