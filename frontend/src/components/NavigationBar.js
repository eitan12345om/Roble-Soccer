import React from 'react'
import {Tab} from 'semantic-ui-react'
import GameCardCollection from "./GameCardCollection";
import DataProvider from "./DataProvider";

const panes = [
  {menuItem: 'Upcoming Games',
    render: () => <Tab.Pane><DataProvider endpoint="api/game"
                                          render={data => <GameCardCollection data={data}/>}/></Tab.Pane>
  },
  {menuItem: 'Past Games', render: () => <Tab.Pane>Tab 2 Content</Tab.Pane>},
  {menuItem: 'Create New Game', render: () => <Tab.Pane>Tab 3 Content</Tab.Pane>},
];

const NavigationBar = () => <Tab panes={panes}/>;

export default NavigationBar;
