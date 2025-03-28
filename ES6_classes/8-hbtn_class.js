export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') { // check if size is a number
      throw new TypeError('Size must be a number');
    }
    if (typeof location !== 'string') { // check if location is a string
      throw new TypeError('Location must be a string');
    }
    /* eslint-disable no-underscore-dangle */
    this._size = size;
    this._location = location;
    /* eslint-enable no-underscore-dangle */
  }

  get size() {
    return this._size; // getter
  }

  get location() {
    return this._location; // getter
  }

  valueOf() {
    return this._size; // method
  }

  toString() {
    return this._location; // method
  }
} // export default HolbertonClass;
