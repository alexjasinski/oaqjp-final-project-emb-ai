// let RunSentimentAnalysis = () => {
//     const textToAnalyze = document.getElementById("textToAnalyze").value;

//     const xhttp = new XMLHttpRequest();

//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             document.getElementById("system_response").innerHTML = xhttp.responseText;
//         }
//     };

//     // Send as POST request with data
//     xhttp.open("POST", "/emotionDetector", true);
//     xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//     xhttp.send("text=" + encodeURIComponent(textToAnalyze));
// }

let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
