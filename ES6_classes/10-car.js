const cloneSymbol = Symbol('clone'); // create a symbol for cloning

export default class Car { // create a class Car
  constructor(brand, motor, color) {
    this._brand = brand; // set the brand of the car
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand; // get the brand of the car
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  [cloneSymbol]() {
    return new this.constructor(this._brand, this._motor, this._color);
  } // clone the car

  cloneCar() {
    return this[cloneSymbol]();
  }
}
