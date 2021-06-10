import React from 'react';
import './index.css';

class ColorChoices extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			data: props.data,
			selected: props.selected
		};
		this.setParentColour = this.setParentColour.bind(this);
	}

	setParentColour = (e) => {
		this.props.callback(e.target.id)
	}

	componentDidUpdate(prevProps) {
		if (this.props.data !== prevProps.data)
			this.setState({"data": this.props.data})
		if (this.props.selected !== prevProps.selected)
			this.setState({"selected": this.props.selected})
	} 

	render() {
		const { data, selected } = this.state;
		return (
			<div className="colorChoices" style={{display: "flex", width: "200px", flexWrap: "wrap"}}>
				{data.map(value => {
					var elementStyle = {backgroundColor: value}
					if(selected === value) {
						elementStyle["border"] = "1px solid"
						elementStyle["margin"] = "1px"
					}
					return <div 
						className="colorChoiceBox" 
						key={value} 
						id={value} 
						style={elementStyle} 
						onClick={e => this.setParentColour(e)}>
					</div>
				})
			}
			</div>
		);
	}
}

export default ColorChoices;
