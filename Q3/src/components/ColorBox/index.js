import React from 'react';
import './index.css';

class ColorBox extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			"color": props.color
		};
	}

	componentDidUpdate(prevProps) {
		if (this.props.color !== prevProps.color)
			this.setState({"color": this.props.color})
	} 

	render() {
		const {color} = this.state;
		return (
			<div className="colorBox" style={{backgroundColor: color}}>
			</div>
		);
	}
}

export default ColorBox;
