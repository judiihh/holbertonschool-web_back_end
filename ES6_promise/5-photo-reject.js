export default function uploadPhoto(filename) { // return a promise
  return Promise.reject(new Error(`${filename} cannot be processed`)); // reject the promise
}
