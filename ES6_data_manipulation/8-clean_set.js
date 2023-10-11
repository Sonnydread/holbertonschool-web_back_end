export default function cleanSet(set, string) {
  const list = [];
  if (string && typeof string === 'string') {
    const arr = Array.from(set);
    arr.forEach((str) => {
      if (str && str.startsWith(string)) { list.push(str.slice(string.length)); }
    });
  }
  return list.join('-');
}
