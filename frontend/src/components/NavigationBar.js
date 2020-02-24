import React from 'react'
import {Tab} from 'semantic-ui-react'
import GameCardCollection from "./GameCardCollection";
import DataProvider from "./DataProvider";
import GameForm from "./GameForm";
import PropTypes from "prop-types";
import Rules from "./Rules";

const panes = [
    {
        menuItem: 'Upcoming Games',
        render: () => <Tab.Pane><DataProvider endpoint="api/game"
                                              render={data => <GameCardCollection data={data}/>}/></Tab.Pane>
    },
    {
        menuItem: 'New Game',
        render: () => <Tab.Pane><GameForm/></Tab.Pane>
    },
    {
        menuItem: 'Past Games',
        render: () => <Tab.Pane><DataProvider endpoint="api/past_games"
                                              render={data => <GameCardCollection data={data}/>}/></Tab.Pane>
    },
    {
        menuItem: 'Rules',
        render: () => <Tab.Pane><Rules/></Tab.Pane>
    },
];

const NavigationBar = () => <Tab panes={panes}/>;

NavigationBar.propTypes = {
    styles: PropTypes.object
};

export default NavigationBar;
