/**
 * Created by Raphael Amponsah on 9/14/2017.
 */

$(document).ready(function () {
    var randDigit = Math.floor(Math.random() * 9000000) + 1000000;
        $("#id_order_id").val("SHC" + randDigit)
})