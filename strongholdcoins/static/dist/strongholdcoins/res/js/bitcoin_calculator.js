/**
 * Created by Raphael Amponsah on 9/14/2017.
 */

$(document).ready(function () {
    var DOLLAR_RATE=4.47;
    var ACTION_FEE;

    var origional_total_rate;
    var amount1 = $("#amount1");
    var amountTotal = $("#amountTotal");
    var amount_of_bitcoins_buying = $("#amount_of_bitcoins1");
    var transaction_rate = parseInt($("#key_fee").val());
    var transaction_fee1 = $("#transaction_fee1");
    var shc_tf = $("#btcview");

    var url = "http://coincap.io/front";

    $.getJSON(url, function (data) {
         data = $.grep(data, function (n, i) {
            return (n.long == "Bitcoin" || n.long == "Ethereum" || n.long == "Litecoin" || n.long == "Dash" || n.long=="Ripple")
        });


         for(d in data){
             $( ".newsticker1" ).append( "<li>"+data[d].long+" ("+data[d].short+") Price:"+data[d].price+"</li>" );
         };







        var selectedAction = $("input[name='coin']");
         $("input[name='action']").on('change',function () {
            switch ($(this).val()){
                case 'Bu':
                    ACTION_FEE=50;
                    break;
                case 'S':
                    ACTION_FEE=25;
                    break;
                case 'I':
                    ACTION_FEE =10;
                    break;
            }



             $("input[name='coin']").on('change', function () {
            if ($(this).val() === 'B') {
               origional_total_rate = data[0].price;
                }else if($(this).val() === 'E'){
                     origional_total_rate = data[1].price;

                }else if($(this).val()==='L'){
                    origional_total_rate = data[2].price;
                }else{
                    origional_total_rate = data[0].price;
                }


            $("#amount1").on('keyup', function () {
            var amt = parseInt(amount1.val());
            var transaction_amount = (amt * ((transaction_rate) / 100));

            var int_origional_total_rate = parseFloat(origional_total_rate);
            amount_of_bitcoins_buying.val(Math.round((amt / int_origional_total_rate) * 10000) / 10000);
            transaction_fee1.val(transaction_amount);

            vt = transaction_fee1.val()+amt;



// (Math.round(((amt + transaction_amount)*DOLLAR_RATE)*100)/100)+ACTION_FEE
            amountTotal.val((Math.round(((amt + transaction_amount)*DOLLAR_RATE)+ACTION_FEE)*100)/100);
            console.log(((amt + transaction_amount)*DOLLAR_RATE)+ACTION_FEE);
        });

        });
        });




        // variables for holding data
        // var origional_total_rate = $("#h_totsfee").val();




    });

});