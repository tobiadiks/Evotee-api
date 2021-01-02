import React, { Component } from 'react';
import Navbar from './Navbar';
import Head from './Head';
    
class Landing extends Component {
    state = {  }
    render() { 
        return (<>
            <Navbar/>
            <Head/>
            </>
        );
}

}
 
export default Landing;