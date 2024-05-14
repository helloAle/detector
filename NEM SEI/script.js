function checkName() {
    var name = document.getElementById("nameInput").value.toLowerCase();
    var result = document.getElementById("result");
    
    if (name === "kaique" || name === "ike" || name === "maiku" || name === "kaiq") {
        result.textContent = "I love him sooooooo much";
    } else {
        result.textContent = "No love detected";
    }
}
