import {Button, Form} from "semantic-ui-react";
import React, {Component} from "react";

class GameForm extends Component {
    constructor(props) {
        super(props);

        this.state = {
            options: [
                {key: 'Roble Field', text: 'Roble Field', value: 'Roble Field'},
                {key: 'Wilbur Field', text: 'Wilbur Field', value: 'Wilbur Field'},
                {key: 'Sand Hill', text: 'Sand Hill', value: 'Sand Hill'},
            ],

            selected: 'Roble Field'
        };
    }

    onChange = (prop, value) => {
        this.setState({
            [prop]: value
        });
    };

    handleSubmission() {
        // e.preventDefault();
        // console.log(e);
        console.log("HERE");
        return;
        const response = fetch('/api/game',
            {
                method: 'POST',
                // body: JSON.stringify({
                //     state.name,
                //     this.state.email
                //     // Other body stuff
                // }),
                headers: {
                    'Content-Type': 'application/json'
                }
            }
        );
    }

    render() {
        return <Form action='/api/game/' onSubmit={this.handleSubmission()}>
            <Form.Dropdown label='Location' placeholder='Select Option' defaultValue={this.state.selected} fluid
                           selection options={this.state.options}/>

            <Form.Group widths='equal'>
                <Form.Field>
                    <label>Max Players</label>
                    <input placeholder='The max number of players for the game'/>
                </Form.Field>
                <Form.Field>
                    <label>Min Players</label>
                    <input placeholder='The min number of players for the game'/>
                </Form.Field>
            </Form.Group>

            <Button type='submit' color='green'>Submit</Button>
        </Form>
    }
}

export default GameForm;
