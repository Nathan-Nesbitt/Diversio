/* 
You don't need to edit this file.

fetchColors is a "fake" API, for the purpose of this code exercise.

It is a Promise which:

- has a 90% chance of resolving to a payload that contains
a random list of colors, with a randomized delay of 0 to 5 seconds.

- has a 10% chance of "timing out" and rejecting.
*/

import { COLOR_LIST } from './colors';

export const fetchColors = new Promise((resolve, reject) => {
	const timeoutDiceRoll = Math.floor(Math.random() * 10);
	if (timeoutDiceRoll === 1) {
		reject('foo');
	} else {
		const timeOut = Math.random() * 5000;
		setTimeout(() => {
			resolve({
				data: {
					colorChoices: _sliceColors(),
					bar: "bin baz"
				}}
				)
		}, timeOut);	
	}
});

const _sliceColors = () => {
	
	let idxOne = Math.floor(Math.random() * COLOR_LIST.length);
	let idxTwo = Math.floor(Math.random() * COLOR_LIST.length);

	if (idxOne === idxTwo) {
		idxTwo += 1;
	}

	let start;
	let end;

	if (idxOne < idxTwo) {
		start = idxOne;
		end = idxTwo;
	} else {
		end = idxOne;
	 	start = idxTwo;
	}

	return COLOR_LIST.slice(start,end);
}
