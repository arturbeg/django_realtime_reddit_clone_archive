$("#list_of_topics").hide()
$(document).ready(function(){


    var roomName = $("#roomName").text();
    var roomAbout = $("#roomAbout").text();

    $("input[id=exampleInputName]").val(roomName);
    $("input[id=exampleInputAbout]").val(roomAbout);













    $("input[name=modelToSearch]").val("localChat");


    $( "#showTopics" ).click(function() {

        console.log("The showTopics is pressed");

        $("#results").empty() // empty instead of hiding !!!!!
        $("#list_of_topics").show()
        $("#list_of_localchats").hide()



        $( "#showLC" ).attr( "class", "" )

        $( "#showT" ).attr( "class", "local_chats_text" )


       $("input[name=modelToSearch]").val("topic");








    });


    $( "#showLocalChats" ).click(function() {

        console.log("The showLocalChats is pressed");

        $("#results").empty()
        $("#list_of_localchats").show()
        $("#list_of_topics").hide()




        $( "#showT" ).attr( "class", "" )

        $( "#showLC" ).attr( "class", "local_chats_text" )


        $("input[name=modelToSearch]").val("localChat");









    });


    /*
    $("#search_chat_form").submit(function() {




        console.log("The form has been submitted");


        q = $("#q").val();

        modelToSearch = $("#modelToSearch").val();

        console.log(q);
        console.log(modelToSearch);



        $("#list_of_localchats").hide();
        $("#list_of_topics").hide();


        load_resource = $("#load_resource").text() + q + "&modelToSearch=" + modelToSearch

        console.log(load_resource)




        $("#results").load(load_resource);


        return false




    });
    */




// Implement real-time search with keyup function

$('#q').keyup(function (event) {




      $("#list_of_localchats").hide();
      $("#list_of_topics").hide();


      var q = $("#q").val()
      var modelToSearch = $("#modelToSearch").val()
      var chatgroup_id = $("#chatgroup_id").val()



      if (q != '' || query != ' ') {
        $.ajax({
           type: 'GET',
           url: '/m/search_chat_room',
           data: {
             'q': q,
             'modelToSearch': modelToSearch,
             'chatgroup_id': chatgroup_id

           },
           success: function(data) {
              $('#results').html(data);
           },
           error: function(data) {
              console.log(data);
           }
         });
      }
    });




    // Removing the element after search
    // and when user clicked another/outside of this element below.

    $(document).click(function(event) {
      $is_inside = $(event.target).closest('#q').length;

      if( event.target.id == 'q' || $is_inside ) {
        return;
      }else {
        $('#results').empty();
      }
    });





// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');




function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});










$('.like').click(function(){
      $.ajax({
               type: "POST",
               url: '/m/like/',
               data: {'message_id': $(this).attr('name')},
               dataType: "json",
               success: function(response) {

                      //alert('Company likes count is now ' + response.likes_count);

                      // Update the likes counter
                      message_id = response.message_id
                      console.log(message_id)
                      $("#" + message_id).text(response.likes_count)


                  //    $("input[name=" + message_id + "]").val("&#xf259;") // issue with flipping the fa icon

                },
                error: function(rs, e) {
                       alert(rs.responseText);
                }
          });
    })











});