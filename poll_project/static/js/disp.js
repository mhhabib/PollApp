
var ctx = document.getElementById("{{poll}}").getContext('2d');
var chart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ["{{ poll.qs_one }}", "{{ poll.qs_two }}", "{{ poll.qs_three }}"],
        datasets: [{
            label: "Poll results",
            backgroundColor: [
                '#ee6f57',
                '#00334e',
                '#206a5d'
            ],
            borderColor: [
                '#a34a39',
                '#00263b',
                '#065446'
            ],
            data: ['{{ poll.qs_one_cnt }}', '{{ poll.qs_two_cnt }}', '{{ poll.qs_three_cnt }}'],
            borderWidth: 1
        }],
    },
    // Configuration options go here
    options: {
        title: {
            display: true,
            text: 'Poll result chart',
            fontSize: 24
        },
        legend: {
            display: true,
            position: 'bottom'
        }
    }
}); 