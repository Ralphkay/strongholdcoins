/**
 * Created by Raphael Amponsah on 10/3/2017.
 */

$(document).ready(function () {
    var url = "http://coincap.io/front";

    $.getJSON( url, function( data ) {

            data = $.grep(data,function (n,i) {
                return (n.long=="Bitcoin" || n.short=="BCH" || n.long=="Ethereum" || n.long=="Litecoin" || n.short=="ETC"||n.long=="Dash")
            });
           labels = [];
           mkdata = [];
           price = [];
        for(l in data){

               labels.push(data[l].long);
               mkdata.push(data[l].mktcap);
               price.push(data[l].price);
           }



           new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
      labels: labels,
      datasets: [{
        label: "Pricing Data",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
        data: price
      }]
    },
    options: {
      title: {
        // display: true,
        text: 'Predicted world cryptocurrency prices'
      }
    }
});

        var ctx = document.getElementById("myChart").getContext('2d');

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labels,
        responsive: true,
        datasets: [{
            label: 'Market Cap (USD)',
            data: mkdata,
            backgroundColor: [
                '#0D91E3',
                '#8e5ea2',
                '#3cba9f',
                '#e8c3b9',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 99, 132, 0.2)'
            ],
            // borderColor: [
            //     'rgba(255, 159, 64, 1)',
            //     'rgba(153, 102, 255, 1)',
            //     'rgba(75, 192, 192, 1)',
            //     'rgba(255, 206, 86, 1)',
            //     'rgba(54, 162, 235, 1)',
            //     'rgba(255,99,132,1)'
            // ],
            borderWidth: 1,

        },
        {
            label: 'Price Data (USD)',
            data: price,

            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,
            type: 'line',
             responsive: true,
            display: true
        }
        ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true,
                    // fontColor:'rgba(255,255,255,0.23)'
                },
                gridLines: {
                    // color:'rgba(255,255,255,0.23)'
                }
            }]
        }
    }
});




    });




});

