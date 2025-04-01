export default function signUpUser(firstName, lastName) { // return a promise
  return Promise.resolve({ // resolve the promise
    firstName, // return the first name
    lastName, // return the last name
  });
}
