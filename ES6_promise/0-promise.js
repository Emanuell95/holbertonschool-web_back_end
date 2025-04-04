function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Promise resolved');
    }, 1000);
  });
}
export default getResponseFromAPI;
