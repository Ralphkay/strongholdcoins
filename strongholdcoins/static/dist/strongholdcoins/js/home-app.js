/**
 * Created by Raphael Amponsah on 10/11/2017.
 */



$(document).ready(function () {

    var URL = "http://coincap.io/front";
    var DOLLAR_RATE=4.47;
    var TAX =1.25;
    var paying_amount = $("#amount");
    var commission_fee = $("#fee");
    var coins = $("#coins");
    var amount2pay = $("#amount2pay");

    $.getJSON(URL, function (data) {
        data = $.grep(data, function (n, i) {
            return (n.long === "Bitcoin" || n.long === "Ethereum" || n.long === "Litecoin");

        });

        $("#cryptoCurrency").on('change', function (e) {

            for (d in data) {
                if ($(this).val().toLowerCase() === data[d].long.toLowerCase()) {
                    var price_of_selected_coin = data[d].price;
                   paying_amount.on("keypress keyup keydown blur change", function(){
                       var cleaned_paying_amount = parseFloat(paying_amount.val());

                       var cleaned_paying_amount_ghc = Math.round((cleaned_paying_amount*4.47)*100)/100;

                       var transaction_fee_paying = Math.round((cleaned_paying_amount_ghc*0.0125)*100)/100;

                       commission_fee.val(transaction_fee_paying);
                       amount2pay.val(cleaned_paying_amount_ghc+transaction_fee_paying);
                       coins.val(Math.round((cleaned_paying_amount/price_of_selected_coin)*100)/100);

                   });


                }
            }
        });
    });





});