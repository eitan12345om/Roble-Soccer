import React from "react";
import PropTypes from "prop-types";
import {Card} from 'semantic-ui-react'
import GameCard from "./GameCard";

const GameCardCollection = ({data}) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        <Card.Group itemsPerRow={3} centered>
            {data.map(game => (
                <GameCard key={game.id} game={game}/>
            ))}
        </Card.Group>
    );

GameCardCollection.propTypes = {
    data: PropTypes.array.isRequired,
};

export default GameCardCollection;
