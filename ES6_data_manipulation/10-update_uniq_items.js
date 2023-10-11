export default function updateUniqueItems(mapa) {
  if (mapa && mapa instanceof Map) {
    for (const [key, value] of mapa) {
      if (value === 1) mapa.set(key, 100);
    }
    return mapa;
  }
  throw new Error('Cannot process');
}
