     $(document).ready(function(){
           $("#mobilemoneyForm").show();
        $("#bankForm").hide();
        $("#id_payment_method").change(function(e) {

            var formType = ($(this).val());
            if (formType == "BAT") {
                $("#bankForm").show();
                $("#mobilemoneyForm").hide();
            } else if (formType == "AMM") {
                $("#mobilemoneyForm").show();
                $("#bankForm").hide();
            } else {
                $("#mobilemoneyForm").show();
                $("#bankForm").hide();
            }
        });
     })