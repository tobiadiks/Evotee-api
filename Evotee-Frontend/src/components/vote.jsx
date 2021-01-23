import React from 'react' 
import {NavBar} from './home'
import bgimage from '../assets/images/bgimage.webp'



class AllPolling extends React.Component {
 
  render() { 
      return (
          
          
        
        <div>
         <VotePage />
         hello
         </div>
          


          




        
          
      );
}

}



class VotePage extends React.Component {
    state = {  }
    render() { 
        return (
            
          <div className="container-fluid bg  ">
          <div className="row">
          
            <div className=" col-12">
           
                <NavBar />

            <h1 className='text-center '> <span className='hi'>Available</span>  <span className='hello'>Elections</span> </h1>

            <Election />


</div>
</div>
            </div>
            
        );
}

}


class Election extends React.Component{

    constructor() {
        super();
        this.state = {
          data: [],
        };
      }


      fetchData() {
        fetch (`http://localhost:8000/api/list/election`)
        
        .then(response => response.json())
        .then((data)=>{
            this.setState({
                data:data
            });
            console.log('fetched' , data[0].electionId);
        });

      }

      componentDidMount() {
        this.fetchData();
      }
    render(){

        
        

        return(

           
             
    
    <div className="container mt-4  ">
            <div className="row">
            {this.state.data.map((v,i)=>
              <div className="col-sm-8 col-md-4 ">
                

              <div className="card my-2" >
        <img className="card-img-top img-fluid" height='200' src={bgimage} alt="Card image cap" />
        <div className="card-body">
          <h5 className="card-title">{v.electionName}</h5>
          <h5 className="card-title">Election Organizer :{v.organizer}</h5>
          <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <a href="#" className="btn btn-primary" onClick={()=>this.fetchData()}>Go somewhere</a>
        </div>
      </div>


              </div>
              )}
            
             
               
            </div>
            
          </div>

    
    
         

         



       
         
      
      
       

           
         

        )
    }
}







 
export   {
 
  AllPolling

};