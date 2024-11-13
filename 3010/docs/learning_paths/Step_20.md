# Step 20

In this step, we’ll break down the components of the `reaction-time.html` file used to create a reaction time experiment that you will participate in for class! Then in step 21, we'll use Pandas to analyze the data we collect.

The reaction time experiment is implemented in JavaScript using the [jsPsych library](https://www.jspsych.org/), designed to help researchers conduct behavioral science experiments in a web browser.

[Click this link to download the `reaction-time.html` file](<files/reaction-time.html>){:download="reaction-time.html"}

In order to read this file, you'll want to move it to a folder in VSCode, and open it there.

Throughout this step, **I don't expect you to be learning JavaScript or jsPsych**. Instead, I want you to see how the principles you've learned in Python programming apply to other languages and tools. By examining the experiment’s structure and components, you’ll see how programming concepts you’ve learned in Python are used in a different context.

We'll also need to cover some basic concepts of experimental design, we'll do that before we dive into the code.

## General Principles of Experimental Design

Let's take a moment to recall (or learn for the first time!) the concepts of the Independent Variable and Dependent Variables in an experiment.

### Independent Variable (IV)

The indepdent variable in the experiment is the thing that is being man**I**pulated - I personally remember this by thinking of the "I" in IV. In the reaction time experiement, the independent variable is the color of the circle that is displayed, which requires a specific key press response from the participant depending on the color of the circle.

### Dependent Variable (DV)

The dependent variable in the experiment is the thing that is being measured - in other words, the thing that *depends* on the manipulated (independent variable). In the reaction time experiment, the dependent variable is the time it takes for the participant to press the correct key after the circle is displayed.

### Control Variables

Control variables are variables that are kept constant throughout the experiment. In the reaction time experiment, the control variables include the size of the circle, the position of the circle on the screen, and the key press that is required for each color.

### Data Collection

When programming an experiment, it's critical to think about how you're collecting your data. We'll look at how the data is collected in the reaction time experiment in the code breakdown.

### Random and Blocked Designs

In the reaction time experiment, there are two different trial types, trials where the circle is blue and trials where the circle is orange. These trials are presented in randomized order, which is a common design in psychology experiments to prevent participants from anticipating the next stimulus.

If you wanted to understand how color similarity might make people respond more slowly, you could have an additional "block" of trials within the experiment where blue and - let's say, a blue-ish purple - are presented as competing colors. This would allow you to examine the difference in reaction time between the two color pairs of blue and purple, and blue and orange.

## Jumping into the JavaScript

> Important code blocks will be highlighted in the following sections, but feel free to explore the entire file! If you want to know how the entire code block works, you give the file to ChatGPT or Copilot and ask the chatbot to explain it to you!

Many of the decisions for the experiment are made *outside* of the code. For example, in this experiment, the colors were chosen to be blue and orange. While we will load images into the experiment to show these colors to the participant when we want to display them, the actual color of the circle is not defined in the code. This is a design decision that was made before the experiment was programmed.

Similarly, it's not written into the code that the color is the IV, and that reaction time is the DV. These are concepts that are understood by the researcher before the experiment is programmed.

Now we'll dive into the pieces of the code that make the experiment run.

### Test Procedure

Below is a block of code within the `JavaScript` called "`test_procedure`", let's break it down:

```javascript
var test_procedure = {
  timeline: [fixation, test],
  timeline_variables: test_stimuli,
  repetitions: 25,
  randomize_order: true
};
```

- `timeline`
    - The `timeline` parameter is an array of objects that represent the sequence of events in the experiment. Here, the `test_procedure` consists of two components: `fixation` and `test`. The `fixation` object displays a fixation cross, while the `test` object presents the colored circle for the participant to respond to.
- `timeline_variables`
    - The `timeline_variables` parameter specifies the stimuli to be used in the experiment. In this case, `test_stimuli` is an array of objects containing the *color of the circle* and the correct response key for each trial.
- `repetitions`
    - The `repetitions` parameter determines how many times the `test_procedure` is repeated. With 25 repetitions, it tells the experiment to show the orange and blue circles 25 times each, meaning that there will be 50 trials in total.
- `randomize_order`
    - The `randomize_order` parameter specifies whether the order of trials should be randomized. When set to `true`, the order of trials is randomized to prevent participants from anticipating the next stimulus.

### Loading Images

This experiment uses two images, preloaded at the start to prevent delays during trials. Preloading is crucial when images need to display instantly. Other designs, like experiments requiring many images or complex visuals, may benefit from a more dynamic image-loading approach.

```javascript
var preload = {
  type: jsPsychPreload,
  images: ['images/blue.png', 'images/orange.png']
};
timeline.push(preload);
```

In simpler terms, this code gets the images ready to be shown at a moment's notice. The `jsPsychPreload` function is used to preload the images, ensuring they are ready for display when needed.

### Data Storage and CSV Export

Data in this experiment is stored in memory by jsPsych, including response accuracy and reaction times. At the experiment’s end, participants see a summary with accuracy and average reaction time. The `jsPsych.data.get().csv()` method then generates a CSV file of the collected data, downloadable via a button.

```javascript
var jsPsych = initJsPsych({
  on_finish: function() {
    jsPsych.data.displayData();
    document.getElementById('download-csv').style.display = 'block';
    document.getElementById('download-csv').onclick = function() {
      var csv = jsPsych.data.get().csv();
      var blob = new Blob([csv], { type: 'text/csv' });
      var url = window.URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'reaction_time_data.csv';
      a.click();
      window.URL.revokeObjectURL(url);
    };
  }
});
```

Let's break down the significant parts of the code block above:

- `jsPsych.data.displayData()`
    - This function displays the data collected during the experiment, showing participants their accuracy and average reaction time.
- `var csv = jsPsych.data.get().csv();`
    - This line generates a CSV file containing the data collected during the experiment.
- `var blob = new Blob([csv], { type: 'text/csv' });`
    - This code block creates a Blob object, which is a file-like object of raw data. In this case, it's a CSV file. A "Blob" is a way to store data that can be downloaded as a file.
- `a.download = 'reaction_time_data.csv';`
    - This line sets the `download` attribute of the anchor element to the desired filename for the downloaded CSV file. This allows the participant to download the data as a CSV file named `reaction_time_data.csv`.

## Connecting JavaScript and jsPsych to Python Principles

This experiment may be in JavaScript, but it uses many programming concepts you've learned in Python, let's think through them:

- **Functions and Initialization**: The function `initJsPsych()` initializes the experiment, just as you've used Python functions to set up programs and prepare data structures.
- **Control Structures (Loops and Conditions)**: The timeline configuration is structured similarly to Python dictionaries and lists. jsPsych uses objects to store multiple settings (analogous to Python’s dictionaries). Loops and conditional logic, like `randomize_order: true`, create flexible procedures, just as you’ve seen in Python loops and conditionals.
- **Trial Data Collection**: The way trial data is collected and stored in `jsPsych.data.get()` is similar to Python data management libraries (like `Pandas`), where you collect, process, and export data. Here, we export as CSV, a format you’ve worked with for storing and analyzing data in Python.
- **Parameter Setting and Modularity**: Each `timeline` component is modular and configured with specific parameters, similar to defining functions with arguments in Python. This modularity in design is essential for scalability and reusability in behavioral science programming.

In summary, although this experiment is in JavaScript, it reinforces core programming concepts: initializing structures, using loops and conditions to control flow, collecting data, and organizing code modularly. 

These are skills you’ll carry into any programming language, allowing you to adapt tools like jsPsych confidently for experimental design.

## Looking for more?

Check out the jsPSych documentation website to learn more about how to use jsPsych for your own experiments: [https://www.jspsych.org/](https://www.jspsych.org/). 