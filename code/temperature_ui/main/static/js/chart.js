function drawData(data, type) {
    window.temp_data = data
    if (type == 1) {
        google.charts.load('current', {
            'packages': ['corechart']
        });
        google.charts.setOnLoadCallback(drawChart, data);

        function drawChart(data) {
            var data = google.visualization.arrayToDataTable(window.temp_data);

            var options = {
                explorer: {
                    actions: ['dragToZoom', 'rightClickToReset'],
                    axis: ['vertical', 'horizontal'],
                    maxZoomIn: 10.0
                },
                hAxis: {
                    title: 'День',
                    titleTextStyle: {
                        color: '#333'
                    }
                },
                vAxis: {
                    minValue: 0,
                },
            };

            var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
            chart.draw(data, options);
        }

    } else if (type == 2) {
        google.charts.load('current', {
            'packages': ['corechart']
        });
        google.charts.setOnLoadCallback(drawChart);

        function drawChart() {
            var data = google.visualization.arrayToDataTable(window.temp_data);

            var options = {
                explorer: {
                    actions: ['dragToZoom', 'rightClickToReset'],
                    axis: ['vertical', 'horizontal'],
                    keepInBounds: true,
                    maxZoomIn: 10.0
                },
                curveType: 'function',
                legend: {
                    position: 'top'
                },
                hAxis: {
                    title: 'День',
                    titleTextStyle: {
                        color: '#333'
                    }
                },
                vAxis: {
                    title: 'Температура, ℃'
                },
            }

            var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
            chart.draw(data, options);
        }
    }

}
