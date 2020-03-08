function drawData() {
    google.charts.load('current', {
        'packages': ['corechart']
    });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Count', 'City_1'],
            ['0', 1000],
            ['0', 1170],
            ['0', 660],
            ['0', 1030]
        ]);

        var options = {
            title: 'Temperature',
            hAxis: {
                title: 'Count',
                titleTextStyle: {
                    color: '#333'
                }
            },
            vAxis: {
                minValue: 0
            },
            width: '100%'
        };

        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
    }

}
