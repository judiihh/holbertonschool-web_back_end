export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    /* eslint-disable no-underscore-dangle */
    this._name = name;
    this._code = code;
    /* eslint-enable no-underscore-dangle */
  }

  get name() {
    return this._name; // getter
  }

  get code() {
    return this._code; // getter
  }

  toString() {
    return `[object ${this._code}]`; // method
  }
} // export default Airport;
