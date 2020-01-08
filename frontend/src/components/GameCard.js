import React from 'react'
import {Card} from 'semantic-ui-react'


const GameCard = (props) => (
    <Card
        href='#card-example-link-card'
        header={props.game.location}
        meta='Friend'
        description={"Max players: " + props.game.max_players}
    />
);

export default GameCard;
