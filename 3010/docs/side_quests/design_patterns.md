# Side Quest: Intro to Design Patterns

## Introduction to Design Patterns

In this Side Quest, we’re introducing **Design Patterns**. These are proven solutions to common problems you’ll encounter in programming. Think of them like templates or blueprints for solving recurring issues in software design.

Design patterns can help make your code more **reusable**, **scalable**, and **understandable**. In scientific programming, we often work with complex data and need our code to be both reliable and flexible. Learning to use design patterns can be a huge advantage.

### What Are Design Patterns?

A **design pattern** is a general, reusable solution to a commonly occurring problem within a given context. Patterns are not complete code but rather templates that guide how we structure and organize code. They fall into three main categories:
1. **Creational Patterns**: These deal with object creation mechanisms.
2. **Structural Patterns**: These focus on organizing objects and classes.
3. **Behavioral Patterns**: These manage communication between objects.

In this step, we'll introduce a few foundational patterns:
- **Singleton**: Ensures only one instance of a class exists.
- **Factory**: Creates instances of different classes based on given conditions.
- **Observer**: Helps objects communicate without being directly linked, useful for experiment settings.

## 1. Singleton Pattern

### What It Does

The **Singleton Pattern** ensures that a class has only one instance and provides a global point of access to it. This pattern is useful when you need exactly one object to coordinate actions across a system.

### Example Use Case: Experiment Settings

Imagine you have a set of parameters for an experiment (e.g., sample size, trial count) that should be consistent across various modules. Singleton can ensure only one settings object exists, avoiding conflicting settings.

### Singleton Implementation

Here’s how we can implement the Singleton pattern in Python:

```python
class ExperimentSettings:
    _instance = None  # To store the unique instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ExperimentSettings, cls).__new__(cls)
            # Set default experiment parameters
            cls._instance.sample_size = 30
            cls._instance.trial_count = 5
        return cls._instance

# Test Singleton behavior
settings1 = ExperimentSettings()
settings2 = ExperimentSettings()

print(settings1 == settings2)  # Should output: True, as both variables point to the same instance
```

This code ensures that `settings1` and `settings2` point to the same instance.

## 2. Factory Pattern

### What It Does

The **Factory Pattern** provides an interface for creating objects but lets subclasses decide which class to instantiate. This pattern is helpful when we want to create different types of objects based on input data without specifying the exact class of object that will be created.

### Example Use Case: Creating Participants with Different Roles

Imagine we’re running a study with participants who have different roles—some are control subjects, others are experimental. The Factory pattern can help us generate different types of participant objects without hardcoding the types.

### Factory Implementation

```python
class Participant:
    def role(self):
        raise NotImplementedError("Subclasses should implement this!")

class ControlParticipant(Participant):
    def role(self):
        return "Control Group"

class ExperimentalParticipant(Participant):
    def role(self):
        return "Experimental Group"

class ParticipantFactory:
    @staticmethod
    def create_participant(participant_type):
        if participant_type == "control":
            return ControlParticipant()
        elif participant_type == "experimental":
            return ExperimentalParticipant()
        else:
            raise ValueError("Unknown participant type")

# Test Factory
control = ParticipantFactory.create_participant("control")
experimental = ParticipantFactory.create_participant("experimental")

print(control.role())       # Outputs: Control Group
print(experimental.role())  # Outputs: Experimental Group
```

This code allows us to create different participant types by simply specifying the type, without needing to know the specific class.

## 3. Observer Pattern

### What It Does

The **Observer Pattern** allows an object (the subject) to notify other objects (observers) when its state changes, without being tightly coupled to them. This is especially useful when several objects need to know about a change in another object’s state, such as notifying modules of a change in experiment status.

### Example Use Case: Real-Time Updates in Experiments

If an experiment progresses in stages, you might want to notify multiple components (e.g., data collection, feedback display) whenever the experiment advances to a new stage.

### Observer Implementation

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclass must implement this method")

class ExperimentDisplay(Observer):
    def update(self, message):
        print(f"Display received update: {message}")

class DataLogger(Observer):
    def update(self, message):
        print(f"DataLogger received update: {message}")

# Test Observer
experiment = Subject()
display = ExperimentDisplay()
logger = DataLogger()

experiment.attach(display)
experiment.attach(logger)

experiment.notify("Experiment started")
experiment.notify("Experiment stage 1 completed")
```

In this example, the `Subject` class maintains a list of observers and notifies them when there’s an update. Each observer (like `ExperimentDisplay` and `DataLogger`) receives the update.

## Reflect

1. Why might these patterns be useful in a psychology-focused programming environment?
2. What are some cases in your own research where these patterns might help?

## Review

In this step, we introduced three foundational design patterns:
- **Singleton**: Ensures only one instance of a class.
- **Factory**: Creates objects based on specific requirements.
- **Observer**: Manages dependencies and notifies multiple objects of changes.

Understanding these patterns is a powerful way to improve the structure and scalability of your code.