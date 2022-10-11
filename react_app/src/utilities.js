// Define our labelmap (list of categories)

const labelMap = {
  1:{name:"Paper", color:'blue'},
  2:{name:"Plastic", color:'orange'},
  3:{name:"Glass", color:'green'},
  4:{name:"Metal", color:'yellow'},
  5:{name:"Organic", color:'black'},
  6:{name:"E-Waste", color:'red'},
  7:{name:"Non-recyclable", color:'purple'},
}

// Define the drawing function

export const drawRect = (boxes, classes, scores, threshold, imgWidth, imgHeight, ctx)=>{
  for(let i=0; i<=boxes.length; i++){
    if(boxes[i] && classes[i] && scores[i]>threshold){

      // Extract variables
      const [y,x,height,width] = boxes[i]
      const text = classes[i]

      // Set styling
      ctx.strokeStyle = labelMap[text]['color']
      ctx.lineWidth = 7
      ctx.fillStyle = 'black'
      ctx.font = '30px Arial'

      // Drawing

      ctx.beginPath()
      ctx.fillText(labelMap[text]['name'] + ' - ' + Math.round(scores[i]*100)/100, x*imgWidth, y*imgHeight-10)
      ctx.rect(x*imgWidth, y*imgHeight, width*imgWidth/2, height*imgHeight/1.5);
      ctx.stroke()

    }
  }
}
