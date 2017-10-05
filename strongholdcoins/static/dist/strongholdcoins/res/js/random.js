/**
 * Created by Raphael Amponsah on 9/14/2017.
 */

$(document).ready(function () {
    var order_id = $("#id_order_id").val();
    if(order_id ===""){
        var randDigit = Math.floor(Math.random() * 9000000) + 1000000;
        console.log(order_id);
        $("#id_order_id").val(randDigit);
    }else if(order_id!==""){
      return order_id;
    }

});/**
 * Created by Raphael Amponsah on 9/14/2017.
 */
