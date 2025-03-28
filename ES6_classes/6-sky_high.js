import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // call the parent class constructor
    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    /* eslint-disable no-underscore-dangle */
    this._floors = floors;
    /* eslint-enable no-underscore-dangle */
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() { // override the parent class method
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
