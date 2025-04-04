function getResponseFromAPI() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve('Promise resolved');
      }, 1000);
    });
  }
  export default getResponseFromAPI;
  

