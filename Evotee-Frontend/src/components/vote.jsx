import React from 'react' 
import {NavBar} from './home'
import bgimage from '../assets/images/bgimage.webp'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  browserHistory
} from "react-router-dom";




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
            
        });

      }

      componentDidMount() {
        this.fetchData();
      }


      checkdata=(e)=>{

        fetch (`http://localhost:8000/api/list/contestant/${e} ` )
        .then(response => response.json())
        .then((data)=>console.log(data))

        
        


       
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
          <h5 className="card-title">{v.electionName} </h5>
          <h5 className="card-title">Election Organizer :{v.organizer}</h5>
          <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          {/* <a href="#" className="btn btn-primary" onClick={()=>this.fetchData()}>Go somewhere</a> */}
          <Link className="btn btn-primary" onClick={()=>this.checkdata(v.electionId)}  to='electiondetail'>Details</Link>
          
        </div>
      </div>


              </div>
              )}
            
             
               
            </div>
            
          </div>

    

        )
    }
}

// Election Details

class Electiondetail extends React.Component{


  constructor() {
    super();
    this.state = {
      election_data: [],
    };
  }



  render(){
    // console.log(this.props.x)
      return(

          <div>
              <h1>Election Details</h1>
              

              <button > checking</button>
              
          </div>
      )
  }
}



// export  {Electiondetail}







 
export   {
 
  AllPolling,
  Electiondetail

};