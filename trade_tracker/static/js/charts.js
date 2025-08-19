document.addEventListener("DOMContentLoaded", function() {
    var ctx = document.getElementById("pnlChart");
    if (ctx) {
        new Chart(ctx, {
            type: "line",
            data: {
                labels: ["Mon","Tue","Wed","Thu","Fri"],
                datasets: [{
                    label: "PnL",
                    data: [100, -50, 200, 75, 0],
                    borderWidth: 2,
                    fill: false,
                    borderColor: "rgb(75, 192, 192)",
                }]
            }
        });
    }
});
