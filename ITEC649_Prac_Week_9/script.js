console.log("Hello it's working!");

console.log(people)

var content = document.getElementById("content");

content.innerHTML = "<p>Hello <b>There</b></p>"

document.getElementById('content').setAttribute('align', 'center');
document.getElementById('content').style.fontSize = '20px';
document.getElementById('content').style.fontFamily = 'Palatino, serif';

var text = "";
for (var person in people) {
    text += " <img src=" + people[person].picture + " alt=\"Smiley face\" height=\"142\" width=\"142\"> " + "<br>";
    text += "ID: " + people[person]._id + "<br>";
    text += "Name: " + people[person].name + " <br>";
    text += "Age: " + people[person].age + "<br>";
    text += "<br>";
}
document.getElementById("content").innerHTML = text;



