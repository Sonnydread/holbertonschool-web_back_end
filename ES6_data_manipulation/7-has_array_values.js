function hasValuesFromArray(set, array) {
  const n = array.map((numero) => set.has(numero));
  const seti = new Set(n);
  return !seti.has(false);
}
export default hasValuesFromArray;
