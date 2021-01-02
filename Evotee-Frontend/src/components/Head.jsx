import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Avatar from '@material-ui/core/Avatar';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

class Head extends Component {
    state = {  }

    componentDidMount(){
        const apiUrl = 'http://localhost:8000/api/election';
        fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => console.log(data));

}
    render() { 
        return ( <div>
            <Grid container
            justify = 'center'
            alignItems = 'center'
            style = {{
                background : '#2241a8'
            }}>
            <Avatar alt = 'evotee'  src = 'ico.gif'  style = {{width: 50,
            height: 50}}/>
            <Typography variant = 'h6' style = {{
                color: '#ffffff',
                fontWeight : '1',
                fontFamily: "monospace"
            }}>free & fair...</Typography>

            </Grid>
          
        </div> );
    }
}
 
export default Head;