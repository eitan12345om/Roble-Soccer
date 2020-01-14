import React, {Component} from 'react'
import {Form} from "semantic-ui-react";

class PlayerForm extends Component {
    constructor(props) {
        super(props);

        this.state = {}
    }

    render() {
        return <Form>
            <Form.Group widths='equal'>
                <Form.Field>
                    <label>Name</label>
                    <input placeholder='First and Last'/>
                </Form.Field>
                <Form.Field>
                    <label>Email</label>
                    <input placeholder='email@example.com'/>
                </Form.Field>
            </Form.Group>
        </Form>
    }
}

export default PlayerForm;
