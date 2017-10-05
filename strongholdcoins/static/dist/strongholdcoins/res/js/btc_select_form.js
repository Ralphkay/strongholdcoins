$(document).ready(function(){
          $("#sellingform").hide();
        $("#selectchoice").change(function(){
            var selectType = ($(this).val());
            if(selectType == "s"){
                $("#sellingform").show();
                $("#buyingform").hide();
            }else{
                 $("#buyingform").show();
                $("#sellingform").hide();
            }
            
        });
      })