class Glass:
    capacity: int = 250

    def __init__(self) -> None:
        self.content: int = 0

    def fill(self, ml: int) -> str:
        if self.content + ml <= Glass.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return f"Glass is now empty"

    def info(self) -> str:
        return f"{Glass.capacity - self.content} ml left"
