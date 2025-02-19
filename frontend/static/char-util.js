function generatePieChart(data) {
     const ctx = document.getElementById('pieChart').getContext('2d');
     const categories = ['News', 'Technology', 'Shopping', 'Education', 'Entertainment'];
     const values = categories.map(() => Math.floor(Math.random() * 100) + 1);
 
     new Chart(ctx, {
         type: 'pie',
         data: {
             labels: categories,
             datasets: [{
                 data: values,
                 backgroundColor: ['#ff6384', '#36a2eb', '#ffce56', '#4caf50', '#ff9800'],
             }]
         }
     });
 }
 