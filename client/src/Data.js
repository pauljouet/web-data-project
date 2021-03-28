const request = require('request')

const fetchData=(filter)=>{
    return new Promise ((resolve, reject)=>{
      try {
        request.get(
          `http://localhost/api/getdata?filter=${filter}`,
          {
            json:true
          }, (err, res, body) => {
            if(err){return console.log(err);}
            let result = body
            resolve(result);
          });
        
      } catch(err){
        console.log("error : ",err);
        reject(err);
      }
    });
  }


module.exports= {fetchData};