dashboard = {
  initDashboardPageCharts: function (weeklyIssueData, monthlyIssueData) {
    var weeklyChartLabels = weeklyIssueData.dates;
    var weeklyChartDataOpened = weeklyIssueData.countsOpened;
    var weeklyChartDataClosed = weeklyIssueData.countsClosed;

    var monthlyChartLabels = monthlyIssueData.months;
    var monthlyChartDataOpened = monthlyIssueData.countsOpened;
    var monthlyChartDataClosed = monthlyIssueData.countsClosed;

    gradientChartOptionsConfigurationWithTooltipPurple = {
      maintainAspectRatio: false,
      legend: {
        display: false,
      },
      tooltips: {
        backgroundColor: "#f5f5f5",
        titleFontColor: "#333",
        bodyFontColor: "#666",
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest",
      },

      responsive: true,
      scales: {
        yAxes: [
          {
            barPercentage: 1.6,
            gridLines: {
              drawBorder: false,
              color: "rgba(29,140,248,0.0)",
              zeroLineColor: "transparent",
            },
            ticks: {
              suggestedMin: 60,
              suggestedMax: 125,
              padding: 20,
              fontColor: "#9a9a9a",
            },
          },
        ],

        xAxes: [
          {
            barPercentage: 1.6,
            gridLines: {
              drawBorder: false,
              color: "rgba(225,78,202,0.1)",
              zeroLineColor: "transparent",
            },
            ticks: {
              padding: 20,
              fontColor: "#9a9a9a",
            },
          },
        ],
      },
    };

    var ctx = document.getElementById("chartLinePurple").getContext("2d");

    var gradientStrokeOpened = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStrokeOpened.addColorStop(1, "rgba(72,72,176,0.1)");
    gradientStrokeOpened.addColorStop(0.4, "rgba(72,72,176,0.0)");
    gradientStrokeOpened.addColorStop(0, "rgba(119,52,169,0)"); //purple colors

    var gradientStrokeClosed = ctx.createLinearGradient(0, 300, 0, 50);

    gradientStrokeClosed.addColorStop(1, "rgba(62,62,176,0.1)");
    gradientStrokeClosed.addColorStop(0.4, "rgba(62,62,176,0.0)");
    gradientStrokeClosed.addColorStop(0, "rgba(259,62,169,0.5)"); //purple colors
    var config = {
      type: "line",
      data: {
        labels: weeklyChartLabels,
        datasets: [
          {
            fill: true,
            backgroundColor: gradientStrokeOpened,
            borderColor: "#d346b1",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: "#d346b1",
            pointBorderColor: "rgba(255,255,255,0)",
            pointHoverBackgroundColor: "#d346b1",
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            label: "Issues Opened",
            data: weeklyChartDataOpened,
          },
          {
            fill: true,
            backgroundColor: gradientStrokeClosed,
            borderColor: "#7dc395",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: "#7dc395",
            pointBorderColor: "rgba(255,255,255,0)",
            pointHoverBackgroundColor: "#7dc395",
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            label: "Issues Closed",
            data: weeklyChartDataClosed,
          },
        ],
      },
      options: gradientChartOptionsConfigurationWithTooltipPurple,
    };

    var myChartData = new Chart(ctx, config);

    // When user clicks the 'Week' button, update the dataset + labels
    $("#0").click(function () {
      var data = myChartData.config.data;
      data.datasets[0].data = weeklyChartDataOpened;
      data.datasets[1].data = weeklyChartDataClosed;
      data.labels = weeklyChartLabels;
      myChartData.update();
    });

    // When user clicks the 'Year - 2020' button, update the dataset + labels
    $("#1").click(function () {
      var data = myChartData.config.data;
      data.datasets[0].data = monthlyChartDataOpened;
      data.datasets[1].data = monthlyChartDataClosed;
      data.labels = monthlyChartLabels;
      myChartData.update();
    });
  },
};
