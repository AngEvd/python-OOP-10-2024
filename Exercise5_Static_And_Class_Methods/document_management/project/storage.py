from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        for category in self.categories:
            if category.id == category_id:
                category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        for document in self.documents:
            if document.id == document_id:
                document.edit(new_file_name)

    def delete_category(self, category_id) -> None:
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)

    def delete_topic(self, topic_id) -> None:
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)

    def delete_document(self, document_id) -> None:
        for document in self.documents:
            if document.id == document_id:
                self.documents.remove(document)

    def get_document(self, document_id) -> "Document":
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self) -> str:
        return f"\n".join(document.__repr__() for document in self.documents)
