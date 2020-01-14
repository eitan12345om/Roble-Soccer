import React from "react";
import ReactDOM from "react-dom";
import NavigationBar from "./NavigationBar";
import {Header, Image, Segment} from "semantic-ui-react";

import logo from '../logo.png';


const styles = {
    primary: {
        success: 'green'
    }
};

const App = () => (
    <div>
        <Segment attached='top'>
            <Header as='h2' textAlign='center'>
                Stanford Soccer
                <Image circular src={logo}/>
            </Header>
        </Segment>

        <Segment attached>
            <NavigationBar styles={styles}/>
        </Segment>
    </div>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App/>, wrapper) : null;

export default App;
