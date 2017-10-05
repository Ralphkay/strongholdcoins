/**
 * Created by Raphael Amponsah on 10/2/2017.
 */
$(document).ready(function () {
    var url = "http://coincap.io/front";

    $.getJSON( url, function( data ) {

            data = $.grep(data,function (n,i) {
                return (n.long=="Bitcoin" || n.long=="Ethereum" || n.long=="Litecoin")
            });
            $("#totsfee").text(data[0].price);
            console.log(data);






    })


});