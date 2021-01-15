import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
// import  Landing from './components/landing';
import {Provider} from 'react-redux'
import store from './store'
import Home from './components/home'

ReactDOM.render(
    <Provider store={store}>
{/* <Landing/> */}
<Home />
    </Provider>

, document.getElementById('root'));