const http = require('http');
const os = require('os');
const fs = require('fs');

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    fs.readFile('index.html', (err, data) => {
      if (err) {
        res.writeHead(500);
        return res.end('Error loading index.html');
      }

      // Get system information
      const hostname = os.hostname();
      const ip = getIPAddress();
      const uptime = formatUptime(process.uptime());
      const totalMem = formatBytes(os.totalmem());
      const freeMem = formatBytes(os.freemem());
      const cpus = os.cpus().length;

      // Replace placeholders in HTML with system information
      let html = data.toString();
      html = html.replace('{hostname}', hostname);
      html = html.replace('{ip}', ip);
      html = html.replace('{uptime}', uptime);
      html = html.replace('{totalMem}', totalMem);
      html = html.replace('{freeMem}', freeMem);
      html = html.replace('{cpus}', cpus);

      // Send response
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.write(html);
      return res.end();
    });
  }
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000/');
});

// Helper functions
function getIPAddress() {
  const interfaces = os.networkInterfaces();
  for (let iface in interfaces) {
    const addresses = interfaces[iface];
    for (let addr of addresses) {
      if (addr.family === 'IPv4' && !addr.internal) {
        return addr.address;
      }
    }
  }
}

function formatUptime(uptime) {
  const hours = Math.floor(uptime / 3600);
  const minutes = Math.floor((uptime - (hours * 3600)) / 60);
  const seconds = Math.floor(uptime % 60);
  return `${hours}h ${minutes}m ${seconds}s`;
}

function formatBytes(bytes, decimals = 2) {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}
