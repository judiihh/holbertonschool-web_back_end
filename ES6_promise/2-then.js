export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => { // then is a method that takes a function and returns a new promise
      console.log('Got a response from the API'); // log the response
      return { status: 200, body: 'success' }; // return the response
    })
    .catch(() => { // catch is a method that takes a function and returns a new promise
      console.log('Got a response from the API'); // log the response
      return new Error(); // return the error
    });
}
