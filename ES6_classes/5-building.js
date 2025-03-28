export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }
    /* eslint-disable no-underscore-dangle */
    this._sqft = sqft;
    /* eslint-enable no-underscore-dangle */

    if (this.constructor !== Building) {
      if (typeof this.evacuationWarningMessage !== 'function') {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
  }

  get sqft() {
    return this._sqft;
  }
}
