document.getElementById("user-form").addEventListener("submit", function(event){
    event.preventDefault();
    alert("Submitting form...");
    const budget=document.getElementById("budget").value;
    const currency=document.getElementById("currency").value;
    const destination = document.getElementById("destination").value;
    if (budget && currency && destination){
        alert("Thank you for submitting! Please wait a minute to make your programme.");
    setTimeout(() => {
      // Refresh the page after a successful submission
      window.location.reload();
    }, 1000);  // Wait 1 second before refreshing
  } else {
    // Simulate failed submission (if form is not filled correctly)
    alert("Failed to submit! Please fill again correctly.");
  }
});
 