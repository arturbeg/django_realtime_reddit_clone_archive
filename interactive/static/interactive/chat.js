$(function() {
    // When we're using HTTPS, use WSS too.
    event.preventDefault()
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chat_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);







    chat_socket.onmessage = function(message) {
        event.preventDefault()
        var data = JSON.parse(message.data);
        console.log('the data has been parsed');


         $('#chat').append('<tr>'
        + '<td>' + data.user.username + '</td>'
        + '<td>' + data.text + '</td>'
        + '</tr>');
        //var chat = $("#chat")
        //var ele = $('<tr></tr>')

        //ele.append(
          //  $("<td></td>").text(data.user)
          //  console.log("The username is received");

       // )
       // ele.append(
         //   $("<td></td>").text(data.text)
            //console.log("The contents of the message are received");
        //)


        //chat.append(ele)
    };





    $("#chatform").on("submit", function(event) {
        event.preventDefault()
        console.log("The button is pressed");
        var message = {
            text: $('#text').val(),
        }


        console.log(message.text);






        chat_socket.send(JSON.stringify(message));
        $("#text").val('').focus();
        return false;
    });
});




