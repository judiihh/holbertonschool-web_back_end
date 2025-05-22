// display the welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// handle input
const handleInput = (data) => {
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\n`);
};

// if the input is a tty, then handle the input
if (process.stdin.isTTY) {
  process.stdin.on('data', handleInput);
} else {
  // if the input is not a tty (piped input), handle input and end event
  process.stdin.on('data', handleInput);
  process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
}
