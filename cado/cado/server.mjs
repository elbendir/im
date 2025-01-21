import { createServer } from 'http';
import { parse } from 'url';

const server = createServer((req, res) => {
  const { pathname } = parse(req.url, true);
  if (pathname === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h1>Bienvenue sur mon site Vercel!</h1>');
  } else {
    res.writeHead(404, { 'Content-Type': 'text/html' });
    res.end('<h1>Page not found</h1>');
  }
});

server.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
