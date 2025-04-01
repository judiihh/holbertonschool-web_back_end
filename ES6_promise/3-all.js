import { uploadPhoto, createUser } from './utils'; // import the functions

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()]) // return a promise
    .then(([photo, user]) => { // destructure the array
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`); // log the response
    })
    .catch(() => { // catch is a method that takes a function and returns a new promise
      console.log('Signup system offline'); // log the response
    });
}
