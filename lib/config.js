var ms   = require('ms');
var os   = require('os');
var path = require('path');
var fs	 = require('fs');

function merge(a, b) {
	for (key in b) {
		if (!a.hasOwnProperty(a)) {
			a[key] = b[key];
		}
	}
	return a;
}

function configPath() {
  if (process.env.NODE_ENV === 'development') {
    return './conf/local.json';
  } else {
    return './conf/prod.json';
  }
}

function userConfig() {
	var userconfpath = path.join(process.env.HOME || process.env.HOMEPATH || process.env.USERPROFILE, '.tldrrc');
	if (fs.existsSync(userconfpath)) {
		return require(userconfpath);
	} else {
		return {};
	}
}

var conf = require(configPath()),
		userconf = userConfig();

conf = merge(userconf, conf); // take user conf as defaults

if (typeof(conf.remote.maxAge) === 'string') {
  conf.remote.maxAge = ms(conf.remote.maxAge) * 1000;
}

conf.proxy = conf.proxy || process.env.HTTP_PROXY || process.env.http_proxy;
conf.updateRepo = conf.updateRepo || "danzimm/tldr-pages";

var CACHE_FOLDER = path.join(process.env.HOME || process.env.HOMEPATH || process.env.USERPROFILE, '.tldr-cache');
conf.local = conf.local || {};
conf.local.cacheFolder = conf.local.cacheFolder || CACHE_FOLDER;

module.exports = conf;
