import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import  Landing from './components/landing';
import {Provider} from 'react-redux'
import store from './store'


ReactDOM.render(
    <Provider store={store}>
<Landing/>
    </Provider>

, document.getElementById('root'));