// Update Booking chart
function updateBookingChart(data, year) {
    console.log(data)
    if ((`year_${year}` in Object.keys(data)) == false) {
        if ($("#booking_charts").length > 0) {
            key=`year_${year}`
            x_values = data[key].months
            y_values = data[key].values

            var options = {
                series: [
                    { name: "Bookings", data: y_values }
                ],
                colors: ["#09CFE8"],
                chart: {
                    type: "bar",
                    height: 300,
                    stacked: true,
                    zoom: { enabled: true },
                },
                responsive: [
                    {
                        breakpoint: 280,
                        options: { legend: { position: "bottom", offsetY: 30 } },
                    },
                ],
                plotOptions: {
                    bar: {
                        dataLabels: {

                            position: "top",
                        },
                        horizontal: false,
                        columnWidth: "30%",
                        borderRadius: 10,
                        borderRadiusApplication: 'end',
                    },
                    
                },
                dataLabels: {
                    enabled: true,
                    style: {
                        colors: ['#333']
                    },
                    offsetY: -20
                  },
                
                xaxis: {
                    categories: x_values,
                },
                legend: { position: "right", offsetY: 0 },
                fill: { opacity: 1 },
            };
            var chart = new ApexCharts(
                document.querySelector("#booking_charts"),
                options
            );
            document.getElementById('booking_charts').innerHTML = ""
            chart.render();
        }
    }
}

// Update Revenue chart
function updateRevenueChart(data, year) {
    console.log(data)
    if ((`year_${year}` in Object.keys(data)) == false) {
        if ($("#revenue_charts").length > 0) {
            key=`year_${year}`
            x_values = data[key].months
            y_values = data[key].values

            var options = {
                series: [
                    { name: "Bookings", data: y_values }
                ],
                colors: ["#28c76f"],
                chart: {
                    type: "bar",
                    height: 300,
                    zoom: { enabled: true },
                },
                responsive: [
                    {
                        breakpoint: 280,
                        options: { legend: { position: "bottom", offsetY: 30 } },
                    },
                ],
                plotOptions: {
                    bar: {
                        dataLabels: {

                            position: "top",
                        },
                        horizontal: false,
                        columnWidth: "30%",
                        borderRadius: 10,
                        borderRadiusApplication: 'end',
                    },
                    
                },
                dataLabels: {
                    enabled: true,
                    style: {
                        colors: ['#333']
                    },
                    offsetY: -20
                  },
                xaxis: {
                    categories: x_values,
                },
                legend: { position: "right", offsetY: 30 },
                fill: { opacity: 1 },
            };
            var chart = new ApexCharts(
                document.querySelector("#revenue_charts"),
                options
            );
            document.querySelector("#revenue_charts").innerHTML = ""
            chart.render();
        }
    }
}
// Update Revenue chart
function updateAnnualRevenueChart(data) {
    console.log(data)
    var options = {
        series: Object.values(data),
            labels: Object.keys(data),
        
        chart: {
            height: 280,
        type: 'polarArea',
        },
        stroke: {
            colors: ['#fff']
        },
        fill: {
            opacity: 0.8
        },
        responsive: [{
            breakpoint: 480,
            options: {
            chart: {
                width: 200
            },
            legend: {
                show: false,
                position: 'center'
            }
            }
        }]
      };

      var chart = new ApexCharts(document.querySelector("#annual_revenue_chart"), options);
      document.querySelector("#annual_revenue_chart").innerHTML = ""
      chart.render();
      
}
