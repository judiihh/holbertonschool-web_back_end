import signUpUser from './4-user-promise'; // import the signUpUser function
import uploadPhoto from './5-photo-reject'; // import the uploadPhoto function

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  // create an array of promises

  return Promise.allSettled(promises).then((results) => results.map((result) => {
    if (result.status === 'fulfilled') {
      return {
        status: result.status,
        value: result.value,
      };
    }
    return {
      status: result.status,
      value: result.reason, // not "reason" but "result.reason"
    };
  }));
}
