from typing import Text


class Lexter:
    def __init__(self, text) -> None:
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        self.current_char == self.text[self.pos] if self.pos < len(self.Text) else None