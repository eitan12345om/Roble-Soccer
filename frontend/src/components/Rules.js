import React from 'react'
import {Container, Divider, Header, List} from 'semantic-ui-react'

const managingRules = [
    "Games can only be called--on or after 3:30pm--the Thursday prior to the desired Saturday",
    "Game managers should specify a start time, minimum and maximum number of players, and a game location",
];

const gamePlayRules = [
    "Players should bring a white and dark shirt",
    "When a ball is 50/50 don't go for it",
    "Everyone must play as goalie",
    "The last player to arrive starts in goal",
    "When using mid-size nets or smaller, goalies must not use their hands unless the ball is shot at the goal",
];

const Rules = () => (
    <Container>
        <Header size='medium' textAlign='left'>Managing the Game</Header>
        <List bulleted items={managingRules}/>

        <Divider/>

        <Header size='medium' textAlign='left'>Game Play</Header>
        <List bulleted items={gamePlayRules}/>

    </Container>
);

export default Rules;
