// This code demonstrates the use of the spread operator in a function.
export default function concatArrays(array1, array2, string) {
    return [...array1, ...array2, ...string];
  }
