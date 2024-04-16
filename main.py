from typing import Any

# Originator
class Editor:
    def __init__(self):
        self._content = ""

    def type(self, words: str):
        self._content += " " + words

    def content(self):
        return self._content

    def save(self):
        return EditorMemento(self._content)


# Memento
class EditorMemento:
    def __init__(self, content: str):
        self._content = content

    def content(self):
        return self._content


# Caretaker
class History:
    def __init__(self):
        self._states = []

    def push(self, state: EditorMemento):
        self._states.append(state)

    def pop(self) -> EditorMemento:
        if self._states:
            return self._states.pop()
        return None


if __name__ == "__main__":
    editor = Editor()
    history = History()

    # Typing content
    editor.type("Hello,")
    editor.type(" world!")

    # Saving state
    history.push(editor.save())

    # Typing more content
    editor.type(" How are you?")

    # Restoring to previous state
    previous_state = history.pop()
    if previous_state:
        editor = Editor()
        editor._content = previous_state.content()

    print("Current content:", editor.content())
