$(function() {

    var TradingAgent = new Object();

    //Tasks
    // Move to meteor


    //Fully vs Parially Observable
    // Perception Action Cycle

    // Deterministic ver stockastic
    // Descrete vs continuous
    // D 
    // buy sell
    //Benign vs adversrial






    // Agent
    // Trading Agent
    // Internal Memory


    // Sensors (input)
    // Control Panel
    // Trade
    // Depth
    // Ticker
    // Lag
    // Trend
    // News
    // Twitter

    // Rates
    // Balance?

    // Actuators (output)
    // Trade
    // Buy
    // Sell

    // Environment
    // Market
    //


    // Perception Action Cycle


    var percentRemaining = 0.994;

    function updateMargins() {

        var $btcPrice = $('#btcPrice'),
            $btcAmount = $('#btcAmount'),
            btcPrice = parseFloat($btcPrice.val()),
            btcAmount = parseFloat($btcAmount.val()),
            btcAmountRemaining = btcAmount * percentRemaining,
            btcCost = btcPrice * btcAmount,
            $btcAmountRemaining = $('#btcAmountRemaining'),
            $btcCost = $('#btcCost'),
            $btcPriceSelling = $('#btcPriceSelling'),
            $btcPriceAsking = $('#btcPriceAsking'),
            $btcProfitAsking = $('#btcProfitAsking'),
            $btcProfitPercentAsking = $('#btcProfitPercentAsking'),
            btcPriceAsking = parseFloat($btcPriceAsking.val());

        $btcAmountRemaining.val(btcAmount * percentRemaining);
        $btcCost.val(numeral(btcCost).format('$0,0.00'));

        // Selling Break Even
        btcAmountRemaining = btcAmountRemaining * percentRemaining;
        var breakEvenPrice = btcCost / btcAmountRemaining;
        $btcPriceSelling.val(numeral(breakEvenPrice).format('$0,0.00'));

        // Asking
        var profit = (btcAmountRemaining * btcPriceAsking) - btcCost;
        var percent = profit / btcCost
        $btcProfitAsking.val(numeral(profit).format('$0,0.00'));
        $btcProfitPercentAsking.val(numeral(percent).format('0%'));

    }

    $("input").on('change', updateMargins);

});