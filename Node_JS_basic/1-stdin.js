process.stdout.write('Welcome to Holberton School, what is your name?\n');
// set the encoding to utf8
process.stdin.setEncoding('utf8');

// Use 'data' event to process incoming chunks
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  const lineEnding = process.stdout.isTTY ? '\r' : '\n';
  process.stdout.write(`Your name is: ${name}${lineEnding}`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
}); // end of end event
