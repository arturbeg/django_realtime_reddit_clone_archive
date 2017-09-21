$(document).ready(function(){



$(".follow_chatgroup").click(function(){



    console.log("A follow button has been clicked")


    $.ajax({
               type: "POST",
               url: '/m/like/',
               data: {},
               dataType: "json",
               success: function(response) {






                },
                error: function(rs, e) {
                       //alert(rs.responseText);
                }
          });


});



});