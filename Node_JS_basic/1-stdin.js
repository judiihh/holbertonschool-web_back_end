process.stdout.write('Welcome to Holberton School, what is your name?\n');

const handleInput = (data) => {
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\n`);
};

if (process.stdin.isTTY) {
  process.stdin.on('data', handleInput);
} else {
  process.stdin.on('data', handleInput);
  process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
}
