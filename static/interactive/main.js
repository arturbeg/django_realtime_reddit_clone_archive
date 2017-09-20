$(document).ready(function(){


    var roomName = $("#roomName").text();
    var roomAbout = $("#roomAbout").text();

    $("input[id=exampleInputName]").val(roomName);
    $("input[id=exampleInputAbout]").val(roomAbout);









    $("#list_of_topics").hide()



    $("input[name=modelToSearch]").val("localChat");


    $( "#showTopics" ).click(function() {

        console.log("The showTopics is pressed");

        $("#results").hide()
        $("#list_of_topics").show()
        $("#list_of_localchats").hide()



        $( "#showLC" ).attr( "class", "" )

        $( "#showT" ).attr( "class", "local_chats_text" )


       $("input[name=modelToSearch]").val("topic");








    });


    $( "#showLocalChats" ).click(function() {

        console.log("The showLocalChats is pressed");

        $("#results").hide()
        $("#list_of_localchats").show()
        $("#list_of_topics").hide()




        $( "#showT" ).attr( "class", "" )

        $( "#showLC" ).attr( "class", "local_chats_text" )


        $("input[name=modelToSearch]").val("localChat");









    });


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









});