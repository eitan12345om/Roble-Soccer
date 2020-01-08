import React from "react";
import ReactDOM from "react-dom";
import NavigationBar from "./NavigationBar";


const App = () => (
    <div>
        <NavigationBar/>
    </div>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App/>, wrapper) : null;
