export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }

  get code() {
    return this._code;
  }

  set code(n) {
    this._code = n;
  }

  get name() {
    return this._name;
  }

  set name(n) {
    this._name = n;
  }
}
