/**
 * Created by Raphael Amponsah on 9/14/2017.
 */

$(document).ready(function () {
    $("#loadit").show();


    var URL = "http://coincap.io/front";
    var DOLLAR_RATE=4.47;
    var ACTION_FEE;
    var origional_total_rate;
    var amount1 = $("#amount1");
    var amountTotal = $("#amountTotal");
    var amount_of_bitcoins_buying = $("#amount_of_bitcoins1");
    var transaction_rate = parseFloat($("#key_fee").val());
    var transaction_fee1 = $("#transaction_fee1");
    var paying_amount = $("#id_order_amount");
    var commission_fee = $("#id_commission_fee");

    $("input[name='order_amount']").attr('readonly',true);
    $("input[name='amount1']").attr('readonly',true);
   var uri = window.location.href;
   var index = uri.lastIndexOf("/");
    var pageExt = uri.substr(index);
    console.log("Page location is " + pageExt);


 if(pageExt==="/edit"){
           $("input[name='order_amount']").attr('readonly',false);
    }


    $.getJSON(URL, function (data) {
         data = $.grep(data, function (n, i) {
            return (n.long === "Bitcoin" || n.long === "Ethereum" || n.long === "Litecoin" || n.long === "Dash" || n.long ==="Ripple")

        });

         for(d in data){
             $( ".newsticker1" ).append( "<li>"+data[d].long+" ("+data[d].short+") Price:"+data[d].price+"</li>" );
         }

        //order_form calculator
        $("input[name='crypto_currency']").on('change', function () {

            $("input[name='order_amount']").attr('readonly',false).focus();

            for(d in data){
                if ($(this).val().toLowerCase() === data[d].long.toLowerCase()){
                    var price_of_selected_coin = data[d].price;
                    // console.log(price_of_selected_coin);
                        paying_amount.on('keyup keypress keydown focus blur change',function () {

                        payment_value_actual = parseFloat($(this).val());

                        var transaction_amount = Math.round((payment_value_actual * ((transaction_rate)))*100)/100;
                        var amount_paying = (payment_value_actual - transaction_amount );
                        var amount_paying_in_dollars = amount_paying/DOLLAR_RATE;
                        var amount_of_cryptcoins = Math.round((amount_paying_in_dollars/price_of_selected_coin)*100)/100;

                       $("#id_amount_of_coins").val(amount_of_cryptcoins);
                       commission_fee.val(transaction_amount);

                        if(pageExt==="/edit"){
                           $("input[name='order_amount']").val();
                    }

                    });

                }
            }
        });


             //Crypto Calculator

             $("input[name='coin']").on('focus blur change click', function () {
                 $("input[name='amount1']").attr('readonly',false).focus();
                 for(d in data){
                    if ($(this).val().toLowerCase() === data[d].long.toLowerCase()) {
                        origional_total_rate = data[d].price;
                     }
                }


                  $("#amount1").on('keyup keypress keydown focus blur change', function () {
                    var amt = parseFloat(amount1.val());
                    var transaction_amount = (amt * ((transaction_rate)));

                    var int_origional_total_rate = parseFloat(origional_total_rate);
                    amount_of_bitcoins_buying.val(Math.round((amt / int_origional_total_rate) * 10000) / 10000);
                    transaction_fee1.val(transaction_amount);

                    vt = transaction_fee1.val()+amt;

                    amountTotal.val((Math.round(((amt + transaction_amount)*DOLLAR_RATE))*100)/100);
                    console.log(((amt + transaction_amount)*DOLLAR_RATE));
            });

        });



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


        $("#mobilemoneyForm").show();
        $("#bankForm").hide();
        var formType = $("#id_payment_method").val();

        var checkFormType =  function(){

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
        };

        $("#id_payment_method").on('change',function(e) {
            var formType = $(this).val();
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

          checkFormType()


    }).done(function() {

        $("#dashboard-loader").fadeOut();
        console.log('Data fetching complete.');
  });



});
