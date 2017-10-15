$(document).ready(function(){
    var DOLLAR_RATE=4.47;
    var url = "http://coincap.io/front";
    var paying_amount = $("#id_order_amount");
    var transaction_rate = parseInt($("#key_fee").val());
    var transaction_fee1 = $("#transaction_fee1");
    $.getJSON(url, function (data) {

        data = $.grep(data, function (n, i) {
            return (n.long === "Bitcoin" || n.long === "Ethereum" || n.long === "Litecoin" )
        });

        $("input[name='crypto_currency']").on('change', function () {
            for(d in data){
                if ($(this).val().toLowerCase() === data[d].long.toLowerCase()){
                    var price_of_selected_coin = data[d].price;
                    // console.log(price_of_selected_coin);
                    paying_amount.on('keyup keypress keydown focus blur change',function () {

                        payment_value_actual = parseInt($(this).val());
                        // payment_value_in_dollars = parseInt($(this).val())/DOLLAR_RATE;

                        var transaction_amount = (payment_value_actual * ((transaction_rate) / 100));
                        var amount_paying = (payment_value_actual - transaction_amount );
                        var amount_paying_in_dollars = amount_paying/DOLLAR_RATE;
                        var amount_of_cryptcoins = Math.round((amount_paying_in_dollars/price_of_selected_coin)*100)/100;

                       $("#id_amount_of_coins").val(amount_of_cryptcoins);
                       console.log($("#id_amount_of_coins").val());
                    });

                }
            }
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
      });