export default function divideFunction(numerator, denominator) { // return a promise
  if (denominator === 0) { // if the denominator is 0
    throw new Error('cannot divide by 0'); // throw an error
  }
  return numerator / denominator; // return the result of the division
}
