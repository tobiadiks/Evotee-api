import React, { Component } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import CssBaseline from '@material-ui/core/CssBaseline';
import MenuIcon from '@material-ui/icons/Menu';






    

class Navbar extends Component {

    state = {  }

    render() {
         
        return (
        
        <>
        <CssBaseline/>
        <AppBar position = 'fixed' color = 'info' style = {{ flexGrow : '1',
    top : 'auto',
    bottom : '0',
    background : '#2241a8'}}>
            <Toolbar>
                <IconButton edge = 'start' color ='inherit' aria-label = 'menu' >
                   <MenuIcon/>
                </IconButton>
           <Button variant = 'outlined' color = 'inherit' style = {{ flexGrow : '1',}}>Vote Now>>></Button>
            </Toolbar>
        </AppBar>
        
        </>

        );
    }
}
 
export default Navbar;