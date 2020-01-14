import React, {Component} from "react";
import PropTypes from "prop-types";

class DataProvider extends Component {
    state = {
        data: [],
        loaded: false,
        placeholder: "Loading..."
    };

    componentDidMount() {
        fetch(this.props.endpoint)
            .then(r => {
                if (r.status !== 200) {
                    return this.setState({placeholder: "Something went wrong. Try refreshing."});
                }

                return r.json();
            })
            .then(data => {
                this.setState({data: data, loaded: true});
                console.log(data);
            })
    }

    render() {
        const {data, loaded, placeholder} = this.state;
        return loaded ? this.props.render(data) : <p>{placeholder}</p>
    }
}

DataProvider.propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired,
};

export default DataProvider;
