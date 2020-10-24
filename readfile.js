const fs = require('fs/promises');
const path = require('path');

async function readDirs(lang) {
    const commonFiles = await fs.readdir('pages/common');
    const linuxFiles = await fs.readdir('pages/linux');
    const osxFiles = await fs.readdir('pages/osx');
    const sunosFiles = await fs.readdir('pages/sunos');
    const windowsFiles = await fs.readdir('pages/windows');
    commonFiles.forEach((fileName) => {
        const src = 'pages/common';
        const dest = 'pages.zh/common';
        const doMv = mv(fileName);
        doMv(src, dest);
    });
    linuxFiles.forEach((fileName) => {
        const src = 'pages/linux';
        const dest = 'pages.zh/linux';
        const doMv = mv(fileName);
        doMv(src, dest);
    });
    osxFiles.forEach((fileName) => {
        const src = 'pages/osx';
        const dest = 'pages.zh/osx';
        const doMv = mv(fileName);
        doMv(src, dest);
    });
    sunosFiles.forEach((fileName) => {
        const src = 'pages/sunos';
        const dest = 'pages.zh/sunos';
        const doMv = mv(fileName);
        doMv(src, dest);
    });
    windowsFiles.forEach((fileName) => {
        const src = 'pages/windows';
        const dest = 'pages.zh/windows';
        const doMv = mv(fileName);
        doMv(src, dest);
    });
}

function mv(fileName) {
    console.log(`check ${fileName}`);
    return async function doMv(src, dest) {
        const srcFilePath = path.join(src, fileName);
        const destFilePath = path.join(dest, fileName);
        const srcStat = await fs.stat(srcFilePath).catch(() => null);
        if (!srcStat) {
            console.log(`source file '${srcFilePath}' is not exist~`);
            return false;
        }
        const destStat = await fs.stat(destFilePath).catch(() => null);
        if (destStat) {
            console.log(`dest file '${destFilePath}' has already existed~`);
            return false;
        }
        copy(srcFilePath, path.join(dest, `todo.${fileName}`));
        return true;
    }

    async function copy(srcFilePath, destFilePath) {
        const buffer = await fs.readFile(srcFilePath);
        fs.writeFile(destFilePath, buffer, { encoding: 'utf-8' }).catch(console.error);
    }
}

readDirs();
