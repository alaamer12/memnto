# Originator class - the object whose state needs to be saved
class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print("Originator: Setting state to", state)
        self._state = state

    def save_to_memento(self):
        print("Originator: Saving state to Memento")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        print("Originator: Restoring state from Memento")

    def __str__(self):
        return f"Originator state: {self._state}"


# Memento class - the object storing the state of the Originator
class Memento:
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


# Caretaker class - responsible for keeping track of multiple mementos
class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


# Example usage
if __name__ == "__main__":
    # Create Originator
    originator = Originator()
    caretaker = Caretaker()

    # Set state and save to memento
    originator.set_state("State 1")
    caretaker.add_memento(originator.save_to_memento())

    # Change state and save to memento
    originator.set_state("State 2")
    caretaker.add_memento(originator.save_to_memento())

    # Restore state from the first memento
    originator.restore_from_memento(caretaker.get_memento(0))
    print(originator)

    # Restore state from the second memento
    originator.restore_from_memento(caretaker.get_memento(1))
    print(originator)
