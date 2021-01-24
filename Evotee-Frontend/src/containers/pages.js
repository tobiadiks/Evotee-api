import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  browserHistory
} from "react-router-dom";

import {AllPolling} from '../components/vote.jsx'
import {Allin} from '../components/home.jsx'
import {Electiondetail} from '../components/vote.jsx'

class ReactRouters extends React.Component{

    render(){
        return(


    <Router >
     <Route exact path='/' component={ Allin} />
     <Route  path='/vote' component={ AllPolling} />
     <Route  path='/electiondetail' component={ Electiondetail} />
                

   </Router>



        )
    }

}

export default ReactRouters;