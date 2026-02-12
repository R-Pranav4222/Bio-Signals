function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition, handleError);
    } else {
      console.log("Geolocation is not supported by this browser.");
    }
  }
  
  function showPosition(position) {
    const lat = position.coords.latitude;
    const long = position.coords.longitude;
    localStorage.setItem("userLocation", JSON.stringify({ lat, long }));
    console.log(`User location: ${lat}, ${long}`);
    
  }
  
  function handleError(error) {
    console.log(`Error occurred. Error code: ${error.code}`);
    switch(error.code) {
      case error.PERMISSION_DENIED:
        console.log("User denied the request for Geolocation.");
        break;
      case error.POSITION_UNAVAILABLE:
        console.log("Location information is unavailable.");
        break;
      case error.TIMEOUT:
        console.log("The request to get user location timed out.");
        break;
      case error.UNKNOWN_ERROR:
        console.log("An unknown error occurred.");
        break;
    }
  }
  
  // Ensure that the getLocation function runs when the window loads
  window.onload = getLocation;
  