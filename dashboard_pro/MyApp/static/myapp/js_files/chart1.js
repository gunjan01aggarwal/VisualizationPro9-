//for chart1 
const ctx1 = document.getElementById('myChart').getContext('2d');

document.getElementById('myChart').width = 800;  // Set width
document.getElementById('myChart').height = 600; // Set height


  new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: chartData1.labels1,
      datasets: [{
        label: '--Country Count--',
        data: chartData1.values1,
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });


//for chart2
document.addEventListener("DOMContentLoaded", () => {
  const ctx2 = document.getElementById('BarChart').getContext('2d');

  document.getElementById('BarChart').width = 800;  // Set width
  document.getElementById('BarChart').height = 400; // Set height

  new Chart(ctx2, {
      type: 'bar',
      data: {
          labels: chartData2.labels2,  // X-axis: Sectors
          datasets: [{
              label: '--Average Intensity varies sector wise--',
              data: chartData2.values2,  // Y-axis: Intensity values
              backgroundColor: 'rgba(54, 162, 235, 0.2)',  // Bar color
              borderColor: 'rgba(54, 162, 235, 1)',        // Border color
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
              x: {
                  title: {
                      display: true,
                      text: 'Sector'
                  }
              },
              y: {
                  beginAtZero: true,
                  title: {
                      display: true,
                      text: ' Average Intensity'
                  }
              }
          }
      }
  });
});

//for chart3
document.addEventListener("DOMContentLoaded", function () {
  const ctx3 = document.getElementById('DoughnutChart');

  document.getElementById('DoughnutChart').width = 800;  // Set width
  document.getElementById('DoughnutChart').height = 400; // Set height
      new Chart(ctx3, {
          type: 'doughnut',
          data: {
              labels: charData3.labels3,  // X-axis: Region names
              datasets: [{
                  label: '--Regional Count--',
                  data: charData3.values3,  // Y-axis: Counts
                  backgroundColor: [
                      'rgba(255, 99, 132, 0.2)',
                      'rgba(54, 162, 235, 0.2)',
                      'rgba(255, 206, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(153, 102, 255, 0.2)',
                      'rgba(255, 159, 64, 0.2)',
                  ],
                  borderColor: [
                      'rgba(255, 99, 132, 1)',
                      'rgba(54, 162, 235, 1)',
                      'rgba(255, 206, 86, 1)',
                      'rgba(75, 192, 192, 1)',
                      'rgba(153, 102, 255, 1)',
                      'rgba(255, 159, 64, 1)',
                  ],
                  borderWidth: 1
              }],
          },
          options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: {
                  legend: {
                      position: 'top',  // Legend position
                  },
                  tooltip: {
                      callbacks: {
                          label: function (context) {
                              const label = context.label || '';
                              const value = context.raw || 0;
                              return `${label}: ${value}`;
                          }
                      }
                  }
              }
          }
      });
  });


//  for chart4

document.addEventListener("DOMContentLoaded", () => {
  const ctx4 = document.getElementById('BarChart2').getContext('2d');

  document.getElementById('BarChart2').width = 600;  // Set width
  document.getElementById('BarChart2').height = 400; // Set height

  new Chart(ctx4, {
      type: 'bar',
      data: {
          labels: chartData4.labels4,  // X-axis: Sectors
          datasets: [{
              label: ' --Average Intensity varies in the start_year--',
              data: chartData4.values4,  // Y-axis: Intensity values
              backgroundColor: 'rgba(54, 162, 235, 0.2)',  // Bar color
              borderColor: 'rgba(54, 162, 235, 1)',        // Border color
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
              x: {
                  title: {
                      display: true,
                      text: 'Start_year'
                  }
              },
              y: {
                  beginAtZero: true,
                  title: {
                      display: true,
                      text: ' Average Intensity'
                  }
              }
          }
      }
  });
});

//for chart5
document.addEventListener("DOMContentLoaded", function () {
  const ctx5 = document.getElementById('LineChart');
  document.getElementById('LineChart').width = 600;  // Set width
  document.getElementById('LineChart').height = 400; // Set height


  new Chart(ctx5, {
          type: 'line',
          data: {
              labels: chartData5.labels5,  // X-axis: Years
              datasets: [{
                  label: '--Intensity varies In the end year--',
                  data: chartData5.values5,  // Y-axis: Intensities
                  fill: false,  // No area under the line
                  borderColor: 'rgba(75, 192, 192, 1)',  // Line color
                  tension: 0.1  // Line smoothness
              }]
          },
          options: {
              responsive: true,
              maintainAspectRatio: false,
              scales: {
                  x: {
                      title: {
                          display: true,
                          text: 'End-Year'
                      }
                  },
                  y: {
                      beginAtZero: true,
                      title: {
                          display: true,
                          text: ' AverageIntensity'
                      }
                  }
              },
              plugins: {
                  legend: {
                      display: true,  // Show legend
                      position: 'top'
                  },
                  tooltip: {
                      callbacks: {
                          label: function (context) {
                              const value = context.raw || 0;
                              return `Intensity: ${value.toFixed(2)}`;
                          }
                      }
                  }
              }
          }
      });
});

//for chart6
document.addEventListener("DOMContentLoaded", function () {
  const ctx6 = document.getElementById('PestleImpactPolarChart');
  document.getElementById('PestleImpactPolarChart').width = 600;  // Set width
  document.getElementById('PestleImpactPolarChart').height = 400; // Set height



  new Chart(ctx6, {
          type: 'polarArea',
          data: {
              labels: polarchartData.labels6,  // Labels: Pestle categories
              datasets: [{
                  label: '--Impact of different pestle categories--',
                  data: polarchartData.values6,  // Values: Impact
                  backgroundColor: [
                      'rgba(255, 99, 132, 0.2)',
                      'rgba(54, 162, 235, 0.2)',
                      'rgba(255, 206, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(153, 102, 255, 0.2)',
                      'rgba(255, 159, 64, 0.2)',
                  ],
                  borderColor: [
                      'rgba(255, 99, 132, 1)',
                      'rgba(54, 162, 235, 1)',
                      'rgba(255, 206, 86, 1)',
                      'rgba(75, 192, 192, 1)',
                      'rgba(153, 102, 255, 1)',
                      'rgba(255, 159, 64, 1)',
                  ],
                  borderWidth: 1
              }]
          },
          options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: {
                  legend: {
                      position: 'top'
                  },
                  tooltip: {
                      callbacks: {
                          label: function (context) {
                              return `${context.label}: ${context.raw.toFixed(2)}`;
                          }
                      }
                  }
              }
          }
      });
});


