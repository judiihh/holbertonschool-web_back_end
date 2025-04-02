import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) { // return a promise
  return Promise.allSettled([
    signUpUser(firstName, lastName), // sign up the user
    uploadPhoto(fileName), // upload the photo
  ]).then((results) => results.map((item) => ({
    status: item.status, // return the status of the promise
    value: item.status === 'fulfilled' ? item.value : item.reason, // return the value of the promise
  })));
}
