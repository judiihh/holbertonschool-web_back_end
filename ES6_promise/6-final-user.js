import signUpUser from './4-user-promise'; // import the signUpUser function
import uploadPhoto from './5-photo-reject'; // import the uploadPhoto function

export default function handleProfileSignup( // return a promise
  firstName,
  lastName,
  fileName,
) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  // create an array of promises
  return Promise.allSettled(promises); // return a promise that resolves to an array of results
}
