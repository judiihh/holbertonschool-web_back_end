export default function guardrail(mathFunction) { // return an array
  const queue = []; // create an empty array
  try {
    queue.push(mathFunction()); // push the result of the mathFunction to the queue
  } catch (error) {
    queue.push(error.toString()); // push the error to the queue
  } finally {
    queue.push('Guardrail was processed'); // push the message to the queue
  }
  return queue; // return the queue
}
// guardrail function takes a mathFunction as an argument and returns an array
// the mathFunction is a function that returns a number
// the guardrail function catches any errors that occur in the mathFunction
// the guardrail function then pushes the error to the queue
// the guardrail function then pushes the message to the queue
// the guardrail function then returns the queue
