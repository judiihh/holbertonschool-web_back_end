import signUpUser from './4-user-promise'; // import the signUpUser function
import uploadPhoto from './5-photo-reject'; // import the uploadPhoto function

export default async function handleProfileSignup( // return a promise
  firstName,
  lastName,
  fileName,
) {
  const promises = [
    signUpUser(firstName, lastName), // sign up the user
    uploadPhoto(fileName), // upload the photo
  ];

  const results = await Promise.allSettled(promises);
  return results.map((result) => ({
    status: result.status, // return the status of the promise
    value: result.status === 'fulfilled' ? result.value : result.reason, // return the value of the promise
  }));
}
