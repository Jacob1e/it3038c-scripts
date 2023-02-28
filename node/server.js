const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
    fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    const myHostName = os.hostname();
    const uptime = os.uptime();
    const totalMem = os.totalmem();
    const freeMem = os.freemem();
    const numCPUs = os.cpus().length;

    const days = Math.floor(uptime / 86400);
    const hours = Math.floor((uptime % 86400) / 3600);
    const minutes = Math.floor((uptime % 3600) / 60);
    const seconds = Math.floor(uptime % 60);

    const html = `
      <!DOCTYPE html>
      <html>
        <head>
          <title>Node JS Response</title>
        </head>
        <body>
          <p>Hostname: ${myHostName}</p>
          <p>IP: ${ip.address()}</p>
          <p>Server Uptime: ${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds</p>
          <p>Total Memory: ${(totalMem / (1024 * 1024)).toFixed(2)} MB</p>
          <p>Free Memory: ${(freeMem / (1024 * 1024)).toFixed(2)} MB</p>
          <p>Number of CPUs: ${numCPUs}</p>
        </body>
      </html>`;
    
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");
