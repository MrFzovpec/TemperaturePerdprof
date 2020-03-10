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
                    title: 'Температура, ℃',
                    titleTextStyle: {
                        color: '#333'
                    }
                }
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
    } else if (type == 3) {
        google.charts.load("current", {
            packages: ["corechart"]
        });
        google.charts.setOnLoadCallback(drawChart);

        function drawChart() {
            var data = google.visualization.arrayToDataTable(window.temp_data);

            var view = new google.visualization.DataView(data);
            view.setColumns([0, 1,
                {
                    calc: "stringify",
                    sourceColumn: 1,
                    type: "string",
                    role: "annotation"
                },
            ]);

            var options = {
                vAxis: {
                    title: '№ Района',
                    titleTextStyle: {
                        color: '#333'
                    }
                },
                hAxis: {
                    title: 'Температура, ℃',
                    titleTextStyle: {
                        color: '#333'
                    }
                },
            };
            var chart = new google.visualization.BarChart(document.getElementById("chart_div"));
            chart.draw(view, options);
        }
    }

}
