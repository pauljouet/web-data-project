const request = require('request')

const fetchMonument=()=>{
    return new Promise ((resolve, reject)=>{
      try {
        request.get(
          'http://localhost/api/monuments',
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

module.exports = {fetchMonument};