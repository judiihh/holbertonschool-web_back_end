process.stdout.write('Welcome to Holberton School, what is your name?\n');
// set the encoding to utf8
process.stdin.setEncoding('utf8');

// Use 'data' event to process incoming chunks
process.stdin.on('data', (data) => {
  // The piped input from 'echo' will include a newline, trim() handles it.
  // The desired output for this EOF test expects a newline at the end.
  process.stdout.write(`Your name is: ${data.toString().trim()}\n`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
}); // end of end event
