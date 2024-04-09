# Python Design Patterns

This repository provides examples of design patterns implemented in Python.

## Design Patterns

Here are some of the most commonly used object-oriented programming (OOP) design patterns:

1. **Singleton Pattern**: This pattern restricts the instantiation of a class to a single instance. It is used to provide a global point of access to the object.
    - Example: A logger class that writes logs to a file. You would want a single instance writing to the file to prevent conflicts.

2. **Factory Pattern**: This pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
    - Example: A pet factory that creates different types of pets (like dogs, cats, etc.) based on the input it receives.

3. **Abstract Factory Pattern**: This pattern provides a way to encapsulate a group of individual factories that have a common theme without specifying their concrete classes.
    - Example: A GUI factory that can create buttons, panels, and windows. You could have a factory for each type of GUI (like Windows, Mac, etc.).

4. **Builder Pattern**: This pattern separates the construction of a complex object from its representation so that the same construction process can create different representations.
    - Example: A car builder that allows you to customize the make, model, color, and number of doors on your car.

5. **Prototype Pattern**: This pattern is used when the type of objects to create is determined by a prototypical instance, which is cloned to produce new objects.
    - Example: An animal clone factory where the prototype of each animal is used to create a new animal of the same type.

6. **Adapter Pattern**: This pattern allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.
    - Example: An adapter that allows you to use a third-party library with a different interface.

7. **Decorator Pattern**: This pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.
    - Example: Python's built-in decorators like @staticmethod, @classmethod, and @property.

8. **Facade Pattern**: This pattern provides a simplified interface to a larger body of code.
    - Example: A database connection manager that provides simple methods for performing database operations.

9. **Observer Pattern**: This pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    - Example: An event management system where the event source updates all registered listeners when an event occurs.

10. **Strategy Pattern**: This pattern enables an algorithm's behavior to be selected at runtime.
    - Example: A sorting algorithm selector that allows the user to choose the sorting algorithm to use on a list of items.
