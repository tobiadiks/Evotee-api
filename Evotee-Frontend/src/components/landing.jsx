import React, { Component } from 'react';
import Navbar from './Navbar';
import Head from './Head';
import Voters from './Voters';
    
class Landing extends Component {
    state = {  }
    render() { 
        return (<>
            <Navbar/>
            <Head/>
            <Voters/>
            </>
        );
}

}
 
export default Landing;