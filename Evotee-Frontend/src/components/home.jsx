import React from 'react'
import bgimg from '../assets/images/bgimage.webp'
import HomeCss from '../assets/css/home.css'
export default class Home extends React.Component{
render(){
    return(


       
       <div >
           <NavBar />
           <VoteBox />
           <RegisterBox />
           {/* <Footer /> */}
        
       </div>
        



    )
}
}


class NavBar extends React.Component{
    render(){


        return(
            <div>

<nav className="navbar navbar-expand-lg navbar-info ">
        <div className="container-fluid">
          <a className="navbar-brand hello ml-2" href="#"><b> EVOTEE</b></a>
          <button className="navbar-toggler hello" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon hello" />
          </button>
          
          <div className="collapse navbar-collapse  "  id="navbarNav">
          <div className='testing'>
            <ul className="navbar-nav">
              <li className="nav-item ">
                  
                <a className="nav-link active hello" aria-current="page" href="#">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link  hello ml-5" href="#">Polling</a>
              </li>
              <li className="nav-item">
                <a className="nav-link hello ml-5" href="#">Prediction  </a>
              </li>
              <li className="nav-item">
                <a className="nav-link hello ml-5" href="#">Previous Results</a>
              </li>
              <li className="nav-item">
                <a className="nav-link  hello ml-5 mr-5" href="#" >About</a>
              </li>
            </ul>
          </div>
        </div>
        </div>
      </nav>

            </div>




        )
    }


}



class VoteBox extends React.Component{
    render(){
        return(
            <div className='voteBox  mt-5' >
                <div className='text-center py-3'>
                    <h6>Election is now Easier <br/> Ballot Anywhere</h6>
                    <div className='py-4 btnv'>
                    <a href="#" class="btn btn-info" role="button" data-bs-toggle="button">Vote Now</a></div>
                    
                </div>
                
            </div>

        )
    }
}




class RegisterBox extends React.Component{
    render(){
        return(
            <div className='RegisterBox  mt-5' >
                <div className='text-center py-3'>
                    <h6>Become an Electorate </h6>
                    <div className='py-4 btnv'>
                    <a href="#" class="btn btn-info" role="button" data-bs-toggle="button">Register</a></div>
                    
                </div>
                
            </div>

        )
    }
}


class Footer extends React.Component{
    render(){
        return(


            <div class="footer">
            <p>Footer</p>
          </div>
        )
    }
}