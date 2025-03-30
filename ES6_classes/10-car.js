export default class Car {
    constructor(brand, motor, color) {
      this._brand = brand;
      this._motor = motor;
      this._color = color;
    }
  
    cloneCar() {
      const Species = Symbol.for('isClone');
      // Get the constructor of the current instance (could be Car or a child class like TestCar)
      const Constructor = this.constructor;
      // Create a new instance of the same class
      const clonedCar = new Constructor();
      
      // Mark it as a clone
      clonedCar[Species] = true;
      
      return clonedCar;
    }
  }