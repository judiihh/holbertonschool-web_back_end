import signUpUser from './4-user-promise'; // import the signUpUser function
import uploadPhoto from './5-photo-reject'; // import the uploadPhoto function

export default function handleProfileSignup(firstName, lastName, fileName) { // return a promise
  return Promise.allSettled([
    signUpUser(firstName, lastName), // sign up the user
    uploadPhoto(fileName), // upload the photo
  ]).then((results) => results.map((result) => ({
    status: result.status, // return the status of the promise
    value: result.status === 'fulfilled' ? result.value : result.reason, // return the value of the promise
  })));
}
