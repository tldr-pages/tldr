var ms   = require('ms');
var path = require('path');
var loader = require('./config-loader');

var conf = loader.get();

// maxAge support for '30 days' and 2592000
if (typeof(conf.remote.maxAge) === 'string') {
  conf.remote.maxAge = ms(conf.remote.maxAge) * 1000;
}

// system-wide proxy
conf.proxy = process.env.HTTP_PROXY || process.env.http_proxy;

// local cache folder
conf.local = {
  cacheFolder: path.join(process.env['HOME'], '.tldr')
}

module.exports = conf;
