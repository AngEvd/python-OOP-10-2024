from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        for index, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {page.index(label) + 1}"
        return "No more free slots"

    def display(self) -> str:
        result = ["-----------"]
        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(11 * "-")
        return "\n".join(result)
