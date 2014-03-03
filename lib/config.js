var ms   = require('ms');
var path = require('path');
var loader = require('./config-loader');

var conf = loader.get();

// system-wide proxy
conf.proxy = process.env.HTTP_PROXY || process.env.http_proxy;

// local cache folder
conf.local = {
  cacheFolder: path.join(process.env['HOME'], '.tldr')
}

module.exports = conf;
