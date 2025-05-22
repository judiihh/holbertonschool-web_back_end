process.stdout.write('Welcome to Holberton School, what is your name?\n');
// set the encoding to utf8
process.stdin.setEncoding('utf8');
// read the input
process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    process.stdout.write(`Your name is: ${chunk.toString().trim()}\n`);
  }
}); // end of readable event

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
}); // end of end event

