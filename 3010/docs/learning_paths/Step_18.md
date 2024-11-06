# Step 18

Up until this point, our course has focused on learning Python. While Python absolutely could be used to build an online research study, as we will see in this Step of the learning path, there are tools better suited to conducting online research.

In this step, we will explore how behavioral science experiments can be conducted on the web. We’ll look at a few web technologies that make this possible, such as `jsPsych`, HTML, CSS, and JavaScript, and provide you with code examples you can try out. We will also introduce tools that allow for online research without requiring any coding (Google Forms).

> Note: This step is meant to conceptually introduce you to a different programming language, specifically JavaScript and web development lanugages (HTML and CSS). We will take a slightly deeper dive into JavaScript in Step 20 when we look at `jsPsych`!

---

## 1. Experiments on the Web

Conducting experiments online allows researchers to reach a broader audience and collect data efficiently. While programming tools like `PsychoPy` (Python) can be used to design experiments, another accessible tool, **`jsPsych`**, simplifies the process of running experiments directly in a web browser.

### What is `jsPsych`?

`jsPsych` is a JavaScript library specifically designed for creating experiments that participants can complete online. It’s flexible, widely used in psychology research, and makes it easier to control and collect data from web-based studies.

### What is JavaScript?

**JavaScript** is a programming language used to create interactive elements on web pages. It’s essential for building dynamic websites and web applications. JavaScript can handle user interactions, animations, and data processing in real-time. 

Have you ever noticed a button change color on a website, or text appear when you hover over an image? These are examples of JavaScript in action!

JavaScript is incredibly versitile for all things on the web, and can be used to create interactive elements, animations, and more. One of my favorite uses of JavaScript is called "ThreeJS" which is a library that allows you to create 3D graphics in the browser! You can check out some examples [here](https://threejs.org/).

---

## 2. Basics of Web Development: HTML, CSS, and JavaScript

To understand how `jsPsych` functions, we’ll cover some core components of web development. Below, we’ll explore HTML, CSS, and JavaScript and provide examples you can try in **VSCode**.

??? Tip "Web Development?"
    Web development can be defined as the process of building websites and web applications. It involves writing code in languages like HTML, CSS, and JavaScript to create interactive and visually appealing web pages. These technologies work together to structure content, style elements, and add interactivity to web pages.

### 2.1. Install Live Server in VSCode

   In the Extensions sidebar, search for **Live Server** and install it. We'll use this extension to run our HTML files in a live server.

---

### 2.2. HTML (HyperText Markup Language)

HTML is the standard language for creating web pages. It allows you to structure content using "tags." A "tag" is a keyword surrounded by angle brackets, like `<tag>`. Tags are used to define elements such as headings, paragraphs, images, and links. A sample of a common tag is `<h1>`, which defines a top-level heading. To close a tag, use a forward slash, like `</h1>`.


Here’s a basic HTML structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Experiment</title>
</head>
<body>
    <h1>Welcome to My Experiment!</h1>
    <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
</body>
</html>
```

> Notice the tags like `<html>`, `<head>`, `<title>`, `<body>`, `<h1>`, and `<p>`. These tags structure the content and define the appearance of the webpage. `<h1>` is a top-level heading, and `<p>` is a paragraph.

This code creates a basic webpage with a title and heading. Copy and paste this code into a new file with an `.html` extension, calling the file `index.html`.

You can open this file in VSCode and use the **Live Server** extension to view it in your browser. To do so, right-click on the HTML file and select **Open with Live Server**.

This will open up a new tab in your browser displaying the HTML content!

---

### 2.3. CSS (Cascading Style Sheets)

CSS styles your HTML content, making it look visually appealing. You can add color, align elements, and much more.

Add the following CSS to your HTML file within a `<style>` tag in the `<head>` section:

```html
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f8ff;
        text-align: center;
    }
    h1 {
        color: #4682b4;
    }
    p {
        color: #2f4f4f;
    }
</style>
```

??? Tip "The full HTML file should now look like this:"
    ```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Experiment</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
            }
            h1 {
                color: #4682b4;
            }
            p {
                color: #2f4f4f;
            }
        </style>
        
    </head>
    <body>
        <h1>Welcome to My Experiment!</h1>
        <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
    </body>

    </html>
    ```

This CSS changes the background color, centers the text, and applies colors to the heading and paragraph.

---

### 2.4. JavaScript

JavaScript adds interactivity to your webpage, such as reacting to user inputs or displaying alerts.

Include this script inside your HTML file’s `<body>` or `<head>` tags:

```html
<script>
    function showAlert() {
        alert("Welcome to the experiment!");
    }
</script>

<button onclick="showAlert()">Click Me</button>
```

This code adds a button that, when clicked, shows an alert message.


??? Tip "Your full HTML file should now look like this:"
    ```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Experiment</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
            }
            h1 {
                color: #4682b4;
            }
            p {
                color: #2f4f4f;
            }
        </style>

        <script>
            function showAlert() {
                alert("Welcome to the experiment!");
            }
        </script>

        <button onclick="showAlert()">Click Me</button>


    </head>
    <body>
        <h1>Welcome to My Experiment!</h1>
        <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
    </body>

    </html>
    ```

---

## 3. Play with Web Development Tools

Now that you've seen the basics of HTML, CSS, and JavaScript, let’s practice combining them to create a simple interactive page.

*Try out the coding exercise below to experiment with web development tools.*

#### 3.1 **Create an HTML file** in VSCode and add the following code:
  
   - This code has HTML, CSS, and JavaScript sections, all within the same file.
   - Run the code using **Live Server** to see the results immediately in your browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            text-align: center;
        }
        h1 {
            color: #4CAF50;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Play with Web Development!</h1>
    <p>Click the button to see a message.</p>
    <button onclick="displayMessage()">Click Me!</button>
    <p id="message"></p>

    <script>
        function displayMessage() {
            document.getElementById("message").innerHTML = "Hello, you're interacting with JavaScript!";
        }
    </script>
</body>
</html>
```


#### 3.2 **Experiment** by changing the following elements:

   - **CSS Colors**: Adjust colors in the CSS styles for `h1`, `body`, or `button`.
   - **Message Text**: Modify the message text in the JavaScript function `displayMessage()`.

This gives you a chance to experiment with the main elements of web development in one file. By changing CSS properties, HTML structure, and JavaScript functions, you’ll start to see how these tools work together.

!!! Tip "`jsPsych` in Step 20"
    When we get to Step 20, we'll take a look of `jsPsych` - but this is a good enough intro for now!

---

## 4. Using Non-Programming Tools for Online Research

For researchers who prefer not to code, tools like **Google Forms** are useful for creating and distributing online surveys. These tools are widely used in psychological and behavioral research to gather self-report data or feedback from participants.

### Designing Effective User Surveys

A **user survey** is a structured way of gathering data about participants' thoughts, behaviors, or experiences. Well-designed surveys can reveal valuable insights into how people feel or think about a topic.

To learn more about designing surveys, visit [How to Design a UX Research Survey](https://dscout.com/people-nerds/how-to-design-a-ux-research-survey), which covers practical tips and best practices for creating effective surveys.

---

## Summary

- **HTML, CSS, and JavaScript** allow us to create and style web-based experiments.
- **Playing with web development tools** helps you learn through hands-on practice, experimenting with colors, structure, and interactivity.
- **Google Forms** and other no-code tools provide options for collecting data without needing to write code.
- **Survey design** is crucial in psychology and UX research to capture reliable and meaningful data from participants.

This step gives you the tools to start exploring web-based research and consider how online experiments can expand your reach and capabilities in behavioral science research.