class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

// Getter and Setter for 'code'
  get code() {
    return this._code;
}

set code(code) {
    if (typeof code === 'string') {
      this._code = code;
    } else {
      throw new TypeError('Code must be a string');
    }
  }

  // Getter and Setter for 'name'
  get name() {
    return this._name;
}

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  // Method to display full currency
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

// Example usage:
const usd = new Currency('USD', 'United States Dollar');
console.log(usd.displayFullCurrency()); // Output: United States Dollar (USD)

// Updating attributes using setters
usd.code = 'EUR';
usd.name = 'Euro';
console.log(usd.displayFullCurrency()); // Output: Euro (EUR)
