export default function loadBalancer(chinaDownload, USDownload) { // return a promise
  return Promise.race([chinaDownload, USDownload]); // return the result of the promise
}
