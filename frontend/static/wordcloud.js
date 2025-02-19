async function generateWordCloud(data) {
     const words = data.map(item => item.query);
     const wordCounts = words.reduce((acc, word) => {
         acc[word] = (acc[word] || 0) + 1;
         return acc;
     }, {});
 
     const formattedWords = Object.keys(wordCounts).map(word => ({
         text: word,
         size: wordCounts[word] * 10
     }));
 
     const layout = d3.layout.cloud()
         .size([600, 400])
         .words(formattedWords)
         .padding(5)
         .rotate(() => ~~(Math.random() * 2) * 90)
         .fontSize(d => d.size)
         .on("end", draw);
 
     layout.start();
 
     function draw(words) {
         d3.select("#wordCloud").html("").append("svg")
             .attr("width", layout.size()[0])
             .attr("height", layout.size()[1])
             .append("g")
             .attr("transform", "translate(300,200)")
             .selectAll("text")
             .data(words)
             .enter().append("text")
             .style("font-size", d => d.size + "px")
             .style("fill", () => `hsl(${Math.random() * 360}, 100%, 50%)`)
             .attr("text-anchor", "middle")
             .attr("transform", d => `translate(${d.x},${d.y})rotate(${d.rotate})`)
             .text(d => d.text);
     }
 }
 