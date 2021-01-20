import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  browserHistory
} from "react-router-dom";

import Vote from '../components/vote.jsx'
import {Home} from '../components/home.jsx'

class ReactRouters extends React.Component{

    render(){
        return(


    <Router >
     <Route exact path='/' component={ Home} />
     <Route  path='/vote' component={ Vote} />
                {/* <Route  path='/slider' component={ Slider} /> */}

   </Router>



        )
    }

}

export default ReactRouters;