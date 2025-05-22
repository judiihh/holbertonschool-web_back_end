process.stdout.write('Welcome to Holberton School, what is your name?\r\n');

process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\r`);
  if (!process.stdin.isTTY) {
    process.stdout.write('\nThis important software is now closing\r\n');
  }
  process.exit();
});
