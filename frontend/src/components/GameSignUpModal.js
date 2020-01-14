import React from 'react'
import {Button, Container, Grid, Modal} from "semantic-ui-react";
import PlayerForm from "./PlayerForm";

const GameSignUpModal = () => (
    <Modal
        trigger={<Button color='green'>Sign Up</Button>}
        header='Sign up!'
        content={<Container><Grid className="segment centered"><PlayerForm/></Grid></Container>}
        actions={[{key: 'done', content: 'Submit', positive: true}]}
    />
);

export default GameSignUpModal;
