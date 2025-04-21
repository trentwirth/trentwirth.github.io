# GD1

> Note: If you skipped the welcome message for the Game Dev Path, please go back and read it! It will help you understand the context of this step. [You can the intro message here](index.md).

## Welcome to the Game Loop

In this step, you'll create your first Phaser game scene and begin learning the basic structure of a JavaScript game. By the end, you'll be able to move a dot (player) by clicking anywhere on the screen and start keeping score by collecting randomly placed objects.

??? Tip "Hold on, what's JavaScript?"
    JavaScript is a programming language that is commonly used for web development. It allows you to create interactive and dynamic content on websites. In the context of game development, JavaScript is often used in conjunction with HTML5 and CSS to create browser-based games. Phaser is a JavaScript framework specifically designed for building 2D games, making it a great choice for our learning path.

    The internet is *built* on JavaScript. If you'd like to learn more, check out Mozilla's [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript).

---

## What You’ll Learn

- How to set up a basic Phaser 3 project using HTML + JavaScript
- Understanding the Phaser game loop (`preload`, `create`, `update`)
- Drawing a simple shape (a circle) on the screen
- Moving the player dot using pointer clicks
- Creating a simple scoring mechanic

---

## Setting Up Your Project

### 1. Create a new folder

Name it something like `gd1-dot-collector`.

### 2. Create an `index.html` file

Paste the following code to create your base project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Dot Collector</title>
  <script src="https://cdn.jsdelivr.net/npm/phaser@3.55.2/dist/phaser.js"></script>
  <style>
    body { margin: 0; }
    canvas { display: block; margin: 0 auto; }
  </style>
</head>
<body>
  <script src="game.js"></script>
</body>
</html>
```


#### Understanding the HTML Structure

When you look at the code above, you are seeing the basic structure of an HTML document. HTML (HyperText Markup Language) is the language that tells web browsers how to display content on a page. Think of it as the blueprint for your game’s web page.

At the very top, the `<!DOCTYPE html>` line tells the browser that this is a modern HTML5 document. Everything inside the `<html>` tags is part of your web page. The `<head>` section contains important information about the page, such as which language it uses, how text should be displayed, and the title that appears in the browser tab.

One key part of the `<head>` is the line that includes the Phaser library using a `<script>` tag. This line connects your project to Phaser, which is the JavaScript framework you’ll use to build your game. By loading Phaser from the internet (using something called a CDN), you don’t have to download anything extra—your game can use Phaser’s features right away.

The `<style>` section is where you can add rules to control how your page looks. In this example, it simply removes extra space around the page and centers the game area.

Finally, the `<body>` section is where the main content of your page goes. Here, you use another `<script>` tag to link to your own JavaScript file (`game.js`). This is where you will write the code that actually makes your game work. When the browser loads your page, it will also load and run your game code.

In summary, the HTML file sets up the environment for your game: it loads the tools you need (like Phaser), provides a place for your game to appear, and connects everything together so your code can run in the browser.

??? Tip "Index? CDN?"
    - **Index**: The `index.html` file is the main entry point for your web application. When you open a folder in a web browser, it looks for an `index.html` file to display by default.
    - **CDN**: A CDN (Content Delivery Network) is a system of distributed servers that deliver web content to users based on their geographic location. By using a CDN, you can load libraries like Phaser quickly and efficiently from servers that are close to you.

### 3. Create a `game.js` file

This is where your game code will live. Copy this basic starter:

```js
const config = {
  type: Phaser.AUTO,
  width: 800,
  height: 600,
  backgroundColor: "#1d1d1d",
  physics: {
    default: 'arcade',
    arcade: {
      debug: false
    }
  },
  scene: {
    preload,
    create,
    update
  }
};

const game = new Phaser.Game(config);

let player;
let score = 0;
let scoreText;

function preload() {}

function create() {
  // Create the player dot
  player = this.add.circle(400, 300, 15, 0x00ffcc);
  this.physics.add.existing(player);
  player.body.setCollideWorldBounds(true);

  // Add score text
  scoreText = this.add.text(16, 16, 'Score: 0', {
    fontSize: '20px',
    fill: '#ffffff'
  });

  // Handle pointer clicks to move player
  this.input.on('pointerdown', (pointer) => {
    this.physics.moveTo(player, pointer.x, pointer.y, 200);
  });
}

function update() {
  // Stop player when it reaches destination
  if (player.body.speed > 0) {
    const distance = Phaser.Math.Distance.Between(
      player.x, player.y,
      player.body.touching.x, player.body.touching.y
    );
    if (distance < 4) {
      player.body.setVelocity(0);
    }
  }
}
```
#### A First Look at JavaScript

JavaScript is a programming language that lets you tell the computer what you want your game to do. It is written using plain text, with a special set of rules (called "syntax") that the computer understands.

When you look at JavaScript code, you’ll see things like:

- **Keywords** (such as `const`, `let`, or `function`) that tell the computer what kind of thing you are making.
- **Variables** (like `player` or `score`) which are names for things you want to keep track of.
- **Functions** (such as `preload`, `create`, and `update`) which are blocks of code that do something specific. You can think of a function as a set of instructions with a name.
- **Curly braces `{}`** are used to group code together, showing where a function or a block of instructions starts and ends.
- **Semicolons `;`** are used to mark the end of a statement, kind of like a period at the end of a sentence.

In the code above, you don’t need to understand every detail yet. For now, just notice that:

- The code is organized into sections, each with a clear purpose (like setting up the game, creating the player, or updating what happens on the screen).
- Words in parentheses `()` are used to give extra information to functions.
- JavaScript is read from top to bottom, and the browser runs it to make your game work.

As you move forward, you’ll learn how to read and write small pieces of JavaScript yourself. For now, just try to get comfortable seeing what the code looks like and understanding that it’s the language your game uses to come to life.

---

## Challenge: Add a Collectable Dot

Now that you have a player dot you can move, let’s add something for the player to collect! We’ll walk through this together, step by step.

### 1. Draw a Collectable Dot

Inside your `create` function, add a new circle to the screen. This will be your collectable. You can use `this.add.circle()` just like you did for the player, but give it a different color. For now, place it at a random position:

```js
// Add this near the top of your file
let collectable;

// Inside the create() function, after creating the player:
const randomX = Phaser.Math.Between(50, 750);
const randomY = Phaser.Math.Between(50, 550);
collectable = this.add.circle(randomX, randomY, 10, 0xffcc00);
this.physics.add.existing(collectable);
```

### 2. Check for Overlap

We want to know when the player touches the collectable. Phaser has a helper for this: `this.physics.add.overlap()`. Add this inside your `create` function:

```js
this.physics.add.overlap(player, collectable, collectDot, null, this);
```

This tells Phaser to call a function named `collectDot` whenever the player and collectable overlap.

### 3. Handle Collecting

Now, let’s write the `collectDot` function. This function should hide the collectable and update the score:

```js
function collectDot(player, collectable) {
  collectable.visible = false; // Hide the dot
  score += 1;
  scoreText.setText('Score: ' + score);
}
```

### 4. Try It Out!

Save your file and refresh your browser. Move your player dot over the collectable. When they touch, the collectable should disappear and your score should go up by one!

---

You just added your first interactive element! If you want to try more, see if you can make the collectable reappear in a new random spot after it’s collected.

---

??? Tip "Full Solution"
    Here’s what your complete `game.js` file could look like after this challenge:

    ```js
    const config = {
      type: Phaser.AUTO,
      width: 800,
      height: 600,
      backgroundColor: "#1d1d1d",
      physics: {
        default: 'arcade',
        arcade: {
          debug: false
        }
      },
      scene: {
        preload,
        create,
        update
      }
    };

    const game = new Phaser.Game(config);

    let player;
    let collectable;
    let score = 0;
    let scoreText;

    function preload() {}

    function create() {
      // Create the player dot
      player = this.add.circle(400, 300, 15, 0x00ffcc);
      this.physics.add.existing(player);
      player.body.setCollideWorldBounds(true);

      // Add score text
      scoreText = this.add.text(16, 16, 'Score: 0', {
        fontSize: '20px',
        fill: '#ffffff'
      });

      // Create the collectable dot at a random position
      const randomX = Phaser.Math.Between(50, 750);
      const randomY = Phaser.Math.Between(50, 550);
      collectable = this.add.circle(randomX, randomY, 10, 0xffcc00);
      this.physics.add.existing(collectable);

      // Check for overlap between player and collectable
      this.physics.add.overlap(player, collectable, collectDot, null, this);

      // Handle pointer clicks to move player
      this.input.on('pointerdown', (pointer) => {
        this.physics.moveTo(player, pointer.x, pointer.y, 200);
      });
    }

    function update() {
      // Stop player when it reaches destination
      if (player.body.speed > 0) {
        const distance = Phaser.Math.Distance.Between(
          player.x, player.y,
          player.body.touching.x, player.body.touching.y
        );
        if (distance < 4) {
          player.body.setVelocity(0);
        }
      }
    }

    function collectDot(player, collectable) {
      collectable.visible = false; // Hide the dot
      score += 1;
      scoreText.setText('Score: ' + score);
    }
    ```

---
## Understanding the Game Loop

Every Phaser game is structured around something called the **game loop**, which runs continuously while the game is active. It's the heart of how your game behaves in real-time — like a director calling cues every frame.

Phaser organizes this loop using **three special functions** that you define:

### `preload()`

This function runs **once**, right before the game starts. You use it to **load assets** that your game will need — things like images, audio, and animations.

In GD1, your game uses simple geometric shapes, so you don’t need to preload anything just yet. That’s why the function is empty for now. But as your games get more complex, this is where you’ll load external files like so:

```js
function preload() {
  this.load.image('dot', 'assets/dot.png');
  this.load.audio('blip', 'assets/sound.wav');
}
```

!!! Tip "The Backpack"
    Think of `preload()` as the "backpack" for your game — it loads everything you might need *before* the game starts.

---

### `create()`

This function runs **once**, immediately after `preload()` finishes. This is where you **set up the initial game world** — things like creating the player, positioning collectables, adding text, or setting up controls.

In your GD1 game, this is where the player dot is created, the collectable is placed, and pointer input is defined.

!!! Tip "The Stage"
    Think of `create()` as setting up the stage: placing actors, props, and initializing everything before the action starts.

---

### `update()`

This function runs **continuously**, many times per second (typically 60 times, or "frames", per second). It’s the **heartbeat** of your game — a repeating loop where you can check for changes, move objects, or respond to conditions.

In GD1, you use `update()` to check if the player has reached their target, and stop their movement if so.

```js
function update() {
  if (player.body.speed > 0) {
    const distance = Phaser.Math.Distance.Between(
      player.x, player.y,
      player.body.touching.x, player.body.touching.y
    );
    if (distance < 4) {
      player.body.setVelocity(0);
    }
  }
}
```

---

## Reflect

- What are the three main lifecycle functions in a Phaser game?
- How does the player move in response to clicks?
- What do you think will happen if you add multiple collectables?

---

## Review

- You built a working game scene from scratch!
- You learned how to move a player around using input
- You practiced setting up and structuring your own Phaser project
- You began keeping score and using simple interactions

---

Next: In **GD2**, you’ll add *multiple* random collectables and detect player collisions to increment the score and re-spawn dots. You'll be building the full foundation of your first playable game!

