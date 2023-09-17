export default function appendToEachArrayValue(array, appendString) {
  const ending = [];
  for (const value of array) {
    ending.push(appendString + value);
  }

  return ending;
}
