import React from "react";
import PropTypes from "prop-types";
import GameCard from "./GameCard";

const GameCardCollection = ({data}) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        <div>
            {data.map(game => (
                <GameCard key={game.id} game={game}/>
            ))}
        </div>
    );

GameCardCollection.propTypes = {
    data: PropTypes.array.isRequired,
};

export default GameCardCollection;
