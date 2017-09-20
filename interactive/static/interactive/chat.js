// Note that the path doesn't matter right now; any WebSocket
// connection gets bumped over to WebSocket consumers

socket = new WebSocket("ws://" + window.location.host + window.location.pathname);






socket.onmessage = function(message) {
        event.preventDefault()
        var data = JSON.parse(message.data);
        console.log('the data has been parsed');


         $('#chat').append(


        '<div class="msg"> <a class="pull-left"> <img class="img-circle" src=" '+ data.profile_avatar  + ' " height="40px" width="40px" ></a> <h5>'
         + data.user + '<span class="time">'+  data.timestamp + '</span></h5><p class="msg_body">'+ data.text + '</span></p></div><div style="clear:both"> </div>'





































         );










// continue when Javascript and JQuery are mastered








         //$('#chat').append('<tr>'
        //+ '<td>' + data.user.username + '</td>'
        //+ '<td>' + data.text + '</td>'
        //+ '</tr>');
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






        socket.send(JSON.stringify(message));
        $("#text").val('').focus();
        return false;
    });
//});




