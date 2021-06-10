# Diversio FE take-home

This is Diversio's front-end take-home exercise.

## How to run

In the project directory, run:

```
yarn install
```
```
yarn start
```

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

## Part 1: build the Color Picker widget

Please implement `ColorWidget` so that:

- [ ] The list of colors returned in the payload of `fetchColors` is shown as available color choices;
- [ ] A user can click a color choice, and see a large box change to that color;
- [ ] The currently selected color is somehow marked (i.e with a black outline);
- [ ] A long list of color choices should render in a sensible way (i.e. perhaps not all on a single row). The boxes should not "jiggle" around as a user clicks them;
- [ ] The app does not crash if fetchColors "fails";

An example solution might look like **color_picker_example_solution.png**.

<img src="https://github.com/DiversioTeam/diversio-fe-exercise/blob/master/color_picker_example_solution.png?raw=true" width="200" />

## Part 2: implement react-redux and redux-saga

The real Diversio app is much more complex, so we use `react-redux` and `redux-saga` in our front end to manage API fetching and making the fetched data available on props to appropriate components.

We rarely make API calls directly within the component itself.

If you are familiar with one or both of these libraries, please showcase this by implementing store, actions, reducers, and/or sagas to do the data fetch instead.

The code that we'd expect you to replace is clearly marked in `ColorWidget`, between `// START OF DATA FETCHING CODE` and `// END OF DATA FETCHING CODE`.

If you are not familiar with these libraries, you may skip part 2.

## How to submit
- [ ] Please make at least one commit containing your changes, and write meaningful commit messages.
- [ ] You can commit to a new git repo and send us the link;
- [ ] Or, you can .zip up the repo, upload to to Google Drive, and share it. (gmail will not allow sending of .zip with .js files inside)
- [ ] Please remove `node_modules` - we will run `yarn install`.

## What we're looking for
This is meant to be a simple task (no gotchas), and reflective of the type of FE work you'd be doing at Diversio. You don't need to do anything fancy. We're looking for:

- Organization and readability in your folder and file structure, JavaScript, JSX, and CSS;
- Thoughtfulness around managing API calls, null values, and error states;
- Well-chosen `camelCase` variable names;
- No warnings in the console related to your code.

If something is unclear, feel free to email. But also, feel free to exercise your best judgement, implement something sensible, and then explain it to us - as you would IRL :)
