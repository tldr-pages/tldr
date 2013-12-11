
// set when testing locally
// will read from localhost instead, and bypass the file cache
exports.test = (process.env.NODE_ENV === 'development');
