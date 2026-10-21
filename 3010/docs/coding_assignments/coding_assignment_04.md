# Coding Assignment 4

> Note: For this assignment you'll need Python and VSCode installed on your own computer (Steps 1 and 3), and you'll use ideas from Steps 1–17 of the Learning Path. **This game will not run in Google Colab**, because Colab can't open a game window.

Most people think games are fun! And a lot of those people have wondered to themselves the following questions:

- How do I make a game?
- Can *I* make a game?
- Would I like making a game?

I know early on in my education, I had wondered all of these things. I also know that I was intimidated by the idea of making a game. I thought it would be too hard, and I didn't know where to start. So in this assignment, you won't start from a blank page. You'll start with a complete, working game, and you'll make it your own.

The game is called **Stroop Smash**, and it's built on one of the most famous findings in psychology: the **Stroop effect**. People are slower to name the *ink color* of a word when the word itself spells a different color. Saying "blue" when you see the word RED printed in blue ink is surprisingly hard! John Ridley Stroop first described this in 1935, and it's still used in research on attention and cognitive control today.

Stroop Smash is a game, but it's also a tiny experiment. Every time you play, it measures your reaction times, shows you *your own* Stroop effect, and saves your data to a CSV file.

**Your job:** get the game running, take a quick tour of the code, then **choose 2 of the 5 upgrades** below and build them.

---

## Part 1: Get the game running (everyone does this)

1. **Install Pygame.** In the VSCode terminal, run:

    ```bash
    pip install pygame
    ```

2. **Download the game:** [Click here to download Stroop Smash](../files/stroop_smash.zip). It comes as a zip file called `stroop_smash.zip`.

3. **Unzip it**, then in VSCode go to `File > Open Folder...` and choose the `stroop_smash` folder.

4. **Run it.** Open `stroop_smash.py` and press the Run button (the triangle in the top right corner), or type this in the terminal:

    ```bash
    python stroop_smash.py
    ```

    > On a Mac, you may need to type `python3` instead of `python`.

5. **Play a full game!** When it's over, look at the end screen. What's your Stroop effect?

6. **Find your data.** In VSCode's file explorer, there's now a `data` folder with a CSV file in it. Open it: each row is one trial. Hang on to it, because this is exactly the kind of data we'll analyze in Steps 20–22.

??? Tip "Trouble installing or running Pygame?"
    - **`ModuleNotFoundError: No module named 'pygame'`, even though you installed it:** your computer probably has more than one Python, and Pygame went into a different one. In the VSCode terminal, run `python -m pip install pygame` (or `python3 -m pip install pygame` on a Mac). This installs Pygame into the same Python that runs your game.
    - **`pip install pygame` fails with a long error:** try the community edition instead: `pip install pygame-ce`. It works exactly the same, and you don't need to change any code.
    - **Nothing happens when you press keys:** click on the game window first so it's selected.

!!! Tip "Make a backup before you change anything"
    Copy the whole `stroop_smash` folder and name the copy `stroop_smash_original`. If you break your game and can't figure out why, you can compare your files with the originals, or start fresh.

---

## Part 2: A quick tour of the code

The game is split into six files, and **each file has one job**:

| File | Its job | Options that use it |
|---|---|---|
| `stroop_smash.py` | **Run this one.** The game loop: the "director" that tells the other files what to do. | 3, 4 |
| `settings.py` | Every setting in one place: colors, keys, timing, number of trials. | 1, 3, 4, 5 |
| `trials.py` | What a trial is, and how the list of trials gets built. | 5 |
| `scoring.py` | How many points each answer is worth. | 2 |
| `display.py` | Everything drawn on the screen. | 3, 4, 5 |
| `results.py` | The end-of-game summary, and saving your data to a CSV. | none |

Splitting code up like this is called **modular programming**, which you first met in Step 12. It means you can change *one* thing, like the scoring rules, without touching the rest of the game. You don't need to understand every line of every file to do this assignment. You only need to understand the parts you change.

!!! Tip "Finding your spot: the `>>> OPTION` markers"
    I've left comments in the code that mark exactly where each option asks you to work. They look like this:

    ```python
    # >>> OPTION 3 (Lives): add a lives attribute here.
    ```

    To find them, open a file, press `Ctrl + F` (`Cmd + F` on Mac), and search for `OPTION 3`. To search every file at once, use `Ctrl + Shift + F` (`Cmd + Shift + F` on Mac).

    Write your new code on the lines **just below** the marker, lined up with the marker's indentation.

---

## Part 3: Choose your two options

| Option | Difficulty | Files you'll change | What you'll practice |
|---|---|---|---|
| **1. New Colors** | ⭐ | `settings.py` | Dictionaries (Step 14) |
| **2. Scoring** | ⭐⭐ | `scoring.py` | `if` / `elif` / `else`, comparisons, `return` (Steps 4, 5, 7) |
| **3. Lives & Game Over** | ⭐⭐⭐ | `settings.py`, `stroop_smash.py`, `display.py` | Attributes (Steps 10–11), conditionals, ending a loop early |
| **4. Beat the Clock** | ⭐⭐⭐⭐ | `settings.py`, `stroop_smash.py`, `display.py` | `while` loops, timing, `max()` (Steps 6, 11) |
| **5. Switch It Up** | ⭐⭐⭐⭐⭐ | `settings.py`, `trials.py`, `display.py` | Classes and methods, random numbers, coordinating changes across files (Steps 10–12) |

Any two options count. The harder ones aren't worth more points, so pick the two that sound the most interesting to you.

### Not sure which to pick? Follow this tree.

```text
START: How are you feeling about Python right now?
│
├── "Honestly, a little nervous."
│     └──> Option 1 + Option 2
│          Small changes, one file at a time. A great way to build confidence.
│
├── "Getting there. I can write an if statement."
│     └──> Option 2 + Option 3
│          You'll go from changing one file to changing three.
│
└── "Pretty confident. Challenge me!"
      │
      └── Should it feel more like an arcade game, or more like a psych experiment?
            ├── Arcade game ───────> Option 3 + Option 4
            └── Psych experiment ──> Option 4 + Option 5
```

!!! Tip "One option at a time, and run the game often"
    Finish and test your first option before you start the second. Inside each option, run the game after every step, not just at the end. If something breaks, you'll know exactly which step caused it.

---

## Option 1: New Colors ⭐

**Files:** `settings.py` · **Practice:** dictionaries (Step 14) · **Rough time:** 15–20 minutes

The game starts with only three colors, on purpose. Your job is to add more.

### Steps

1. **Open `settings.py` and find the `COLORS` dictionary.** Each color is a key-value pair: the key is the color's name (like `"RED"`), and the value is another small dictionary holding its `"rgb"` (what the ink looks like) and its `"key"` (the keyboard key players press for it).

2. **Add at least two new colors.** The easiest way is to copy the `"BLUE"` line, paste it on a new line right below it (still above the closing `}`), and change three things: the name, the rgb numbers, and the key. For example:

    ```python
    COLORS = {
        "RED":   {"rgb": (235, 70, 70),   "key": "r"},
        "GREEN": {"rgb": (60, 200, 95),   "key": "g"},
        "BLUE":  {"rgb": (80, 140, 255),  "key": "b"},
        "PINK":  {"rgb": (255, 105, 180), "key": "p"},   # a new color!
    }
    ```

    > The `PINK` example doesn't count toward your two. Pick your own!

3. **Choose the rgb numbers.** Search "color picker" in Google. It shows a color's RGB value, like `rgb(255, 105, 180)`. Put those three numbers in parentheses.

4. **Choose a key.** Every color needs its own key. The first letter is easiest to remember, but watch out for clashes: BLUE, BLACK, and BROWN all start with B. If two colors share a key, the game will tell you when you run it.

5. **Save and run the game.** Your new colors should appear on the start screen, in the key reminder at the bottom of the screen, and as ink colors during the game. You didn't have to change any of those places yourself: they all read from `COLORS`. That's modular code at work!

### You're done when...

- The game has at least 5 colors (the 3 starters plus at least 2 of yours)
- Each new color has its own key, and pressing it works
- Each new color is easy to read on the dark background, and easy to tell apart from the others
- The game runs from start to finish with no errors

??? Tip "Hint: I can barely see my new color"
    Dark colors like black, navy, or dark brown disappear on the dark background. Make them brighter (use bigger rgb numbers), or try changing `BACKGROUND_COLOR`. If you change the background, check that every other color still looks good on it!

??? Tip "Common errors and how to fix them"
    - **`SyntaxError: invalid syntax. Perhaps you forgot a comma?`** Every color line inside `COLORS` needs a comma at the end.
    - **`SyntaxError: '{' was never closed`** You deleted or moved a curly brace. Each color line needs its own `{` and `}`, and the whole dictionary ends with a `}` on its own line.
    - **The terminal says "Stroop Smash found a problem in settings.py"** I wrote a checker that catches common mistakes. Read the message carefully: it tells you which color has a problem and what's wrong.

??? Question "Think about it: what if two colors look alike?"
    Imagine adding ORANGE right next to RED. Now players are slow for two reasons: Stroop interference, *and* the colors are hard to tell apart. That second problem has nothing to do with the Stroop effect! This is why researchers choose their stimulus colors carefully: they want to measure one thing at a time.

??? Tip "Extra (optional): play with the other settings"
    Try changing `NUM_TRIALS` or `PERCENT_CONGRUENT`. What happens to your Stroop effect when 90% of the trials are congruent? Researchers have studied exactly this question. Search "proportion congruent effect" if you're curious.

---

## Option 2: Scoring ⭐⭐

**Files:** `scoring.py` · **Practice:** `if` / `elif` / `else`, comparison operators, functions that `return` (Steps 4, 5, 7) · **Rough time:** about 30 minutes

Right now, each correct answer is worth exactly 1 point. Boring! Design a better scoring system.

### Steps

1. **Open `scoring.py`.** Read the docstring inside `points_for_trial()`. It lists the information about each trial that you can use in your rules, like `trial.correct` and `trial.rt_ms`.

2. **Replace the body of the function** (the `if` / `else` part) with your own rules. Your scoring system must:
    - give correct answers **at least 10 points**
    - give a **speed bonus** for correct answers faster than a cutoff you choose
    - **take away points** for wrong answers

3. **Explain your rules** in a comment at the top of the function, so someone reading your code knows how scoring works.

4. **Save and play.** After every answer, the feedback screen shows how many points you earned, like "+15 points" or "-5 points". Use it to test each of your rules.

### You're done when...

- A wrong answer shows negative points
- A slow correct answer shows your normal points
- A fast correct answer shows your bonus points
- A comment explains your rules

??? Tip "Hint 1: the shape of the code"
    ```python
    def points_for_trial(trial):
        if not trial.correct:
            return ___          # a wrong answer
        elif trial.rt_ms < ___:
            return ___          # a fast, correct answer
        else:
            return ___          # a correct answer that wasn't fast
    ```

    Why check for wrong answers first? Python checks the conditions in order, and as soon as a function reaches `return`, it stops. So by the time Python reaches the `elif`, it already knows the answer was correct.

??? Tip "Hint 2: picking your speed cutoff"
    Play one game and look at your average times on the end screen. Pick a cutoff a little faster than your average, so the bonus feels earned.

??? Tip "Extra challenge (optional): reward the hard trials"
    Mismatched words (like RED in blue ink) are harder, and for those trials `trial.congruent` is `False`. Can you give them extra points?

    Hint: instead of returning a number right away, make a `points` variable, add to it with `+=` (Step 6) for each bonus that applies, and `return points` at the very end.

??? Tip "Common errors and how to fix them"
    - **`TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'`** For some kind of trial, your function didn't return a number. Every path through your `if` / `elif` / `else` needs a `return`.
    - **`TypeError: '<' not supported between instances of 'NoneType' and 'int'`** (This only happens if you're also doing Option 4.) Trials where the player ran out of time have no reaction time, so `trial.rt_ms` is `None`. Check `if not trial.correct` *first*, as in Hint 1, and timed-out trials will never reach your speed check.

---

## Option 3: Lives & Game Over ⭐⭐⭐

**Files:** `settings.py`, `stroop_smash.py`, `display.py` · **Practice:** attributes (Steps 10–11), conditionals (Step 5), ending a loop early · **Rough time:** about 45 minutes

Right now, you can't lose. Let's add some stakes: players start with 3 lives, lose one for every wrong answer, and get a "Game Over!" when they run out.

**How it works:** The game keeps track of everything that changes while you play (the score, the trial number) in a `GameState` object, defined at the top of `stroop_smash.py`. You'll add `lives` to that object, and then use it in a few places.

### Steps

1. **Add a setting.** In `settings.py`, at the bottom under "YOUR NEW SETTINGS", add:

    ```python
    STARTING_LIVES = 3
    ```

2. **Give the game state some lives.** In `stroop_smash.py`, find the `GameState` class and its `__init__` method. Below the `OPTION 3` marker, create an attribute called `self.lives` and set it to `settings.STARTING_LIVES`. Look at how `self.score` is created a few lines above for the pattern.

3. **Lose a life.** In the `play_game()` function, find the first `OPTION 3` marker. Write an `if` statement: if the trial was *not* correct, subtract 1 from `state.lives`.

4. **Show the lives on screen.** In `display.py`, find the `draw_hud()` method. Its first line of code draws the score. Copy that line, paste it below the `OPTION 3` marker, and change it to draw the lives at the **top center** of the screen: change the text to show `state.lives`, use `self.center_x` for x, keep 32 for y, and remove the `align="left"` part (the default is centered).

    > **Run the game now!** You should see your lives go down when you make a mistake. The game won't end yet; that's the next step.

5. **End the game when lives run out.** Back in `play_game()`, find the second `OPTION 3` marker (it comes after the feedback is shown). Write an `if` statement: if `state.lives` is 0, `break`.

    !!! Tip "New tool: `break`"
        `break` immediately ends the loop it's inside. Python skips straight to the first line after the loop. Here, that means the game jumps to summarizing your results and saving your data, so the trials you *did* play still get saved.

6. **Say "Game Over!"** In the `main()` function, find the `OPTION 3` marker. If `state.lives` is 0, change `title` to `"Game Over!"`.

### You're done when...

- The screen shows "Lives: 3" at the start of the game
- Each wrong answer lowers your lives by 1
- When lives reach 0, the game ends right after the "Oops!" screen, and the end screen says "Game Over!"
- If you make it through every trial with lives left, the end screen still says "Game complete!"
- After a Game Over, the CSV contains only the trials you actually played

??? Tip "Hint for Step 2"
    ```python
    self.lives = settings.STARTING_LIVES
    ```
    Make sure this line is indented to match `self.score = 0`. That puts it inside `__init__`.

??? Tip "Hint for Step 3"
    ```python
    if not trial.correct:
        state.___ -= 1
    ```

??? Tip "Hint for Step 5: where exactly does it go?"
    It goes inside the `for trial in trials:` loop, at the very end, lined up with the `wait(settings.FEEDBACK_MS, clock)` line above it. Putting it *after* the feedback means players see "Oops!" before the game ends, instead of the game just vanishing.

??? Tip "Common errors and how to fix them"
    - **`AttributeError: 'GameState' object has no attribute 'lives'`** Step 2 is missing, has a typo, or isn't indented inside `__init__`.
    - **`AttributeError: module 'settings' has no attribute 'STARTING_LIVES'`** Step 1 is missing, wasn't saved, or is spelled differently. Capital letters matter!
    - **`SyntaxError: 'break' outside loop`** Your `if` statement from Step 5 isn't indented inside the `for` loop.
    - **The game ends after your first mistake, or never ends:** check that your condition is `state.lives == 0` (two equals signs), and that the `break` is indented *inside* your `if`.

---

## Option 4: Beat the Clock ⭐⭐⭐⭐

**Files:** `settings.py`, `stroop_smash.py`, `display.py` · **Practice:** `while` loops and timing (Step 6), attributes (Step 11), `max()` · **Rough time:** about 60 minutes

Right now, players can take as long as they want. Add a time limit that starts out generous and **shrinks** every time the player answers correctly. Run out of time, and it's "Too slow!"

**How it works:** In `stroop_smash.py`, look at the `run_trial()` function. Its Step 3 is a `while waiting:` loop that keeps checking for a key press until `waiting` becomes `False`. Two things will help you:

- `start_time` holds the moment the word appeared, in milliseconds.
- `pygame.time.get_ticks()` gives you the time *right now*, in milliseconds.

So `pygame.time.get_ticks() - start_time` is how long the player has been staring at the word.

Some of the work is already done for you: every trial already has a `timed_out` attribute (it starts as `False`), the feedback screen already says "Too slow!" when it's `True`, and the CSV already saves it.

### Steps

1. **Add three settings.** In `settings.py`, under "YOUR NEW SETTINGS":

    ```python
    START_TIME_LIMIT_MS = 2000   # the first word gives you 2 seconds
    MIN_TIME_LIMIT_MS = 700      # the limit never gets shorter than this
    SPEED_UP_MS = 100            # each correct answer takes this much off the limit
    ```

2. **Give the game state a time limit.** In `stroop_smash.py`, in `GameState.__init__`, below the `OPTION 4` marker, create `self.time_limit_ms` and set it to `settings.START_TIME_LIMIT_MS`.

3. **Check the clock (the tricky part).** In `run_trial()`, find the `OPTION 4` marker. Write code that:

    - calculates how long it's been since the word appeared, and stores it in a variable called `elapsed_ms`
    - checks whether the player is *still waiting* **and** `elapsed_ms` is greater than or equal to `state.time_limit_ms`
    - if so: sets `trial.timed_out` to `True`, sets `trial.correct` to `False`, and sets `waiting` to `False` (which ends the `while` loop)

    !!! Warning "Watch your indentation!"
        This code goes **inside** the `while waiting:` loop, but **outside** the `for event in ...` loop. Line it up with the marker comment and with `clock.tick(240)`:

        ```python
        while waiting:
            for event in pygame.event.get():
                ...                          # checks for key presses (already written)

            # >>> OPTION 4 (Beat the Clock): check the time limit here.
            # your code goes here, lined up with this comment

            clock.tick(240)
        ```

    Why check that the player is still waiting? They might have pressed a key during this same pass through the loop. You don't want to mark a real answer as "Too slow!"

    > **Run the game now!** Don't press anything when a word appears. After 2 seconds, you should see "Too slow!"

4. **Speed things up.** In `play_game()`, find the `OPTION 4` marker. If the trial was correct, lower `state.time_limit_ms` by `settings.SPEED_UP_MS`, but never let it go below `settings.MIN_TIME_LIMIT_MS`.

    The `max()` function makes this easy: it returns the bigger of the numbers you give it. For example, `max(700, 650)` gives you `700`, so the limit can never sink below 700.

5. **Show the time limit on screen.** In `display.py`, in `draw_hud()`, find the `OPTION 4` marker. Draw the time limit in seconds, like "Time limit: 1.8 s", just below the score. Copy the score line as your starting point, then:

    - use `self.small_font` and `settings.HINT_COLOR` so it's smaller and grayer than the score
    - keep x at 24 and `align="left"`, but change y to 64
    - to turn milliseconds into seconds, divide by 1000. Inside an f-string, `:.1f` shows one decimal place: `f"{1850 / 1000:.1f}"` gives `"1.9"`

### You're done when...

- If you don't press anything, "Too slow!" appears after about 2 seconds, and it counts as a wrong answer
- The time limit on screen shrinks after each correct answer
- The time limit never goes below `MIN_TIME_LIMIT_MS`
- In the CSV, timed-out trials show `True` in the `timed_out` column and an empty `rt_ms`

??? Tip "Hint for Step 3: fill in the blanks"
    ```python
    elapsed_ms = pygame.time.get_ticks() - ___
    if waiting and elapsed_ms >= ___:
        trial.timed_out = ___
        trial.correct = ___
        waiting = ___
    ```

??? Tip "Hint for Step 4: fill in the blanks"
    ```python
    if trial.correct:
        state.time_limit_ms = max(___, state.time_limit_ms - ___)
    ```

??? Tip "Common errors and how to fix them"
    - **"Too slow!" only shows up when you move the mouse:** your time check is indented *inside* the `for event in ...` loop. That loop only runs when something happens (a key press, a mouse movement), so your check only runs then too. Move it out one level, as shown in the Step 3 warning.
    - **"Too slow!" appears instantly on every word:** check your `START_TIME_LIMIT_MS`. It's in milliseconds, so 2 seconds is `2000`, not `2`.
    - **`AttributeError: 'GameState' object has no attribute 'time_limit_ms'`** Step 2 is missing, has a typo, or isn't indented inside `__init__`.
    - **`TypeError: '<' not supported between instances of 'NoneType' and 'int'`** You're also doing Option 2, and your scoring checks `trial.rt_ms` before checking whether the answer was correct. See Option 2's common errors.

??? Question "Think about it: the speed–accuracy tradeoff"
    As the time limit shrinks, do you make more mistakes? Look at the `correct` column in your CSV from start to finish. Psychologists call this the **speed–accuracy tradeoff**: when people are pushed to go faster, they usually make more errors.

??? Tip "Extra challenge (optional): a shrinking timer bar"
    Can you draw a bar under the word that gets shorter as time runs out? You'd need to redraw the screen *inside* the `while waiting:` loop, using `pygame.draw.rect()` with a width that depends on `elapsed_ms`. This one is genuinely hard. Try it only if you're feeling bold!

---

## Option 5: Switch It Up ⭐⭐⭐⭐⭐

**Files:** `settings.py`, `trials.py`, `display.py` · **Practice:** classes and methods (Steps 10–11), random numbers, coordinating changes across files (Step 12) · **Rough time:** 60–90 minutes

Add a second rule to the game. Most words work like they do now: answer with the *ink* color. But when a word appears **inside a box**, players must answer with what the word *says*. Players have to switch between two rules, which psychologists call **task switching**. The extra time it takes to change rules is called a **switch cost**.

**How it works:** Every trial needs to know which rule it uses. You'll give each `StroopTrial` a `rule` attribute (either `"ink"` or `"word"`), randomly choose some trials to use the word rule, change what counts as the correct answer, and draw a box around word-rule trials.

Here's the nice part: the feedback screen and the answer checking both ask the trial for its `correct_answer()`. Once you fix that one method, everything that uses it updates automatically. Modular code paying off!

### Steps

1. **Add a setting.** In `settings.py`, under "YOUR NEW SETTINGS":

    ```python
    PERCENT_WORD_RULE = 25   # % of trials where you answer the WORD, not the ink
    ```

2. **Give every trial a rule.** In `trials.py`, in `StroopTrial`'s `__init__`, below the `OPTION 5` marker, create `self.rule` and set it to `"ink"`. Every trial starts with the normal rule.

3. **Change the correct answer.** In the `correct_answer()` method, add an `if` statement *before* `return self.ink`: if `self.rule` is `"word"`, return `self.word` instead.

4. **Choose some trials to use the word rule.** In the `make_trials()` function, find the `OPTION 5` marker. `random.randint(1, 100)` gives you a random whole number from 1 to 100. If that number is less than or equal to `settings.PERCENT_WORD_RULE`, set `trial.rule` to `"word"`.

    > Why does this work? A random number from 1 to 100 is 25 or less about 25% of the time.

5. **Save the rule in your data.** In the `to_dict()` method, below the `OPTION 5` marker, add `"rule": self.rule,` to the dictionary.

    > **Run the game now!** It should work, and sometimes the "correct" answer will be the word. But there's no box yet, so players can't tell which rule to use! Let's fix that.

6. **Draw the box.** In `display.py`, find the `draw_stimulus()` method and its `OPTION 5` marker. If `trial.rule` is `"word"`, draw a rectangle around the word. You'll need two new tools:

    - `word_rect.inflate(50, 30)` gives you a copy of the word's rectangle that's 50 pixels wider and 30 pixels taller, so the box doesn't touch the letters.
    - `pygame.draw.rect(self.screen, color, rectangle, width=4)` draws the outline of a rectangle, 4 pixels thick. (Try leaving off `width=4` to see why we need it!)

7. **Explain the new rule.** In `display.py`, find the `draw_instructions()` method. Add a new string to the `lines` list, below the `OPTION 5` marker, explaining the box rule. The start screen draws every string in that list, so adding one is all it takes.

### You're done when...

- About 1 in 4 words appears inside a box
- For boxed words, pressing the key for the *word* counts as "Correct!"
- If you get a boxed word wrong, the feedback names the word as the right answer
- The start screen explains the box rule
- Your CSV has a `rule` column

??? Tip "Hint for Step 3"
    ```python
    def correct_answer(self):
        """Return the color name the player SHOULD press for this trial."""
        if self.rule == ___:
            return ___
        return self.ink
    ```

??? Tip "Hint for Step 4"
    ```python
    if random.randint(1, 100) <= settings.___:
        trial.rule = ___
    ```
    This goes inside the `for` loop, lined up with `trial = StroopTrial(word, ink)`.

??? Tip "Hint for Step 6"
    ```python
    if trial.rule == "word":
        box = word_rect.inflate(50, 30)
        pygame.draw.rect(self.screen, settings.TEXT_COLOR, ___, width=4)
    ```

??? Tip "Hint for Step 7"
    Every string in a list needs a comma after it:
    ```python
    lines = [
        "A color word will flash on the screen.",
        "Press the key for the INK color, not the word!",
        "Your new line goes here!",
    ]
    ```

??? Tip "Common errors and how to fix them"
    - **`AttributeError: 'StroopTrial' object has no attribute 'rule'`** Step 2 is missing, or isn't indented inside `__init__`.
    - **`AttributeError: module 'settings' has no attribute 'PERCENT_WORD_RULE'`** Step 1 is missing, wasn't saved, or is spelled differently.
    - **Boxed words are always marked wrong:** the spelling of `"word"` must match *exactly* (all lowercase) in every place you use it: `trials.py` in two places, and `display.py`.
    - **Boxes appear, but answers are still checked by ink color:** your `if` in Step 3 must come *before* `return self.ink`. Once Python reaches a `return`, the method stops.

??? Question "Think about it: is there a switch cost?"
    Open your CSV and compare the `rt_ms` values for rows where `rule` is `word` to rows where it's `ink`. Are boxed trials slower? You'll learn how to answer questions like this properly with Pandas in Step 21.

---

## Part 4: Submitting (if you're taking this for credit)

Submit these on Canvas:

1. **Your game folder, zipped**, named `lastname_firstname_coding_assignment_4.zip`. Include your `data` folder!
    - Windows: right-click the folder, then choose `Compress to ZIP file` (or `Send to > Compressed (zipped) folder`).
    - Mac: right-click the folder, then choose `Compress`.

2. **One screenshot for each option, showing it working.** For example: your new colors on the start screen, a "+15 points" message, a "Game Over!" screen, a "Too slow!" message, or a boxed word.
    - Windows: `Windows + Shift + S`. Mac: `Cmd + Shift + 4`.

3. **A short write-up**, a few sentences for each option, answering:
    - Which files did you change, and what did you change in each one? Explain it in your own words.
    - What broke along the way, and how did you fix it? (If nothing broke, what would you try adding next?)

---

## Just for fun: more ideas

Finished and want to keep going? None of these are required.

- **Sound effects:** look up `pygame.mixer.Sound` to play a sound for correct and wrong answers.
- **A high score that's remembered:** save the best score to a JSON file and load it at the start of each game (Step 13).
- **Neutral trials:** add trials that show `XXXX` in a color. Researchers use these as a baseline: are they faster or slower than matching words?
- **Analyze your data:** load your CSV files with Pandas and make a histogram of your reaction times (Steps 16 and 19).

Congratulations, you've modified a real game! And now you know the answers to those questions at the top: this is how a game is made, and yes, *you* can make one.