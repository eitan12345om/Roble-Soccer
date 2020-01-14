import React from 'react'
import {Card} from 'semantic-ui-react'
import PropTypes from "prop-types";
import GameSignUpModal from "./GameSignUpModal";


const GameCard = (props) => (
    <Card
        fluid={false}
        header={props.game.location}
        meta={String(props.game.datetime)}  // FIXME
        description={"Max players: " + props.game.max_players}
        extra={<GameSignUpModal/>}
    />
);

GameCard.propTypes = {
    game: PropTypes.shape({
        location: PropTypes.string.isRequired,
        datetime: PropTypes.string.isRequired,
        max_players: PropTypes.number.isRequired,
        min_players: PropTypes.number.isRequired,
    }),
};

export default GameCard;
