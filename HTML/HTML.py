from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def iterate(self):
        pass


class HTMLIterator(Iterator):
    def __init__(self, html_element):
        self.html_element = html_element

    def iterate(self):
        yield from self._iterate_element(self.html_element)

    def _iterate_element(self, element):
        yield element
        if isinstance(element, ContainerElement):
            for child in element.children:
                yield from self._iterate_element(child)


class ElementState(ABC):
    @abstractmethod
    def handle(self):
        pass


class VisibleState(ElementState):
    def handle(self):
        print("Element is visible.")


class HiddenState(ElementState):
    def handle(self):

        print("Element is hidden.")


class HTMLElement:
    def __init__(self, tag_name, content):
        self.tag_name = tag_name
        self.content = content
        self.state = VisibleState()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def render(self):

        return f'<{self.tag_name}>{self.content}</{self.tag_name}>'

    def on_created(self):

        print(f"Element {self.tag_name} created.")

    def on_inserted(self):

        print(f"Element {self.tag_name} inserted into the document.")

    def on_removed(self):
        print(f"Element {self.tag_name} removed from the document.")


class TextElement(HTMLElement):
    def render(self):
        return super().render()


class ImageElement(HTMLElement):
    def __init__(self, src):
        super().__init__('img', '')
        self.src = src

    def render(self):
        return f'<{self.tag_name} src="{self.src}">'


class ContainerElement(HTMLElement):
    def __init__(self, tag_name):
        super().__init__(tag_name, [])
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        children_html = ''.join([child.render() for child in self.children])
        return f'<{self.tag_name}>{children_html}</{self.tag_name}>'


if __name__ == "__main__":from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def iterate(self):
        pass


class HTMLIterator(Iterator):
    def __init__(self, html_element):
        self.html_element = html_element

    def iterate(self):
        yield from self._iterate_element(self.html_element)

    def _iterate_element(self, element):
        yield element
        if isinstance(element, ContainerElement):
            for child in element.children:
                yield from self._iterate_element(child)


class ElementState(ABC):
    @abstractmethod
    def handle(self):
        pass


class VisibleState(ElementState):
    def handle(self):
        print("Element is visible.")


class HiddenState(ElementState):
    def handle(self):
        print("Element is hidden.")


class HTMLElement:
    def __init__(self, tag_name, content):
        self.tag_name = tag_name
        self.content = content
        self.state = VisibleState()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def render(self):
        return f'<{self.tag_name}>{self.content}</{self.tag_name}>'

    def on_created(self):
        print(f"Element {self.tag_name} created.")
        self._on_created_hook()

    def _on_created_hook(self):
        pass

    def on_inserted(self):
        print(f"Element {self.tag_name} inserted into the document.")
        self._on_inserted_hook()

    def _on_inserted_hook(self):
        pass

    def on_removed(self):
        print(f"Element {self.tag_name} removed from the document.")
        self._on_removed_hook()

    def _on_removed_hook(self):
        pass


class TextElement(HTMLElement):
    def render(self):
        return super().render()

    def _on_created_hook(self):
        print(f"Text content '{self.content}' rendered for {self.tag_name} element.")


class ImageElement(HTMLElement):
    def __init__(self, src):
        super().__init__('img', '')
        self.src = src

    def render(self):
        return f'<{self.tag_name} src="{self.src}">'

    def _on_created_hook(self):
        print(f"Image element with src '{self.src}' created.")


class ContainerElement(HTMLElement):
    def __init__(self, tag_name):
        super().__init__(tag_name, [])
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        children_html = ''.join([child.render() for child in self.children])
        return f'<{self.tag_name}>{children_html}</{self.tag_name}>'

    def _on_created_hook(self):
        print(f"Container element '{self.tag_name}' created.")


if __name__ == "__main__":
    text_element = TextElement('p', 'Hello, World!')
    text_element.on_created()
    print(text_element.render())

    image_element = ImageElement('example.jpg')
    image_element.on_created()
    print(image_element.render())

    container_element = ContainerElement('div')
    container_element.add_child(text_element)
    container_element.add_child(image_element)
    container_element.on_created()
    print(container_element.render())

    text_element.set_state(HiddenState())
    text_element.on_removed()
    print(text_element.get_state().handle())


    print("\nIterating through HTML document:")
    html_iterator = HTMLIterator(container_element)
    for element in html_iterator.iterate():
        print(element.render())


    text_element = TextElement('p', 'Hello, World!')
    text_element.on_created()
    print(text_element.render())


    image_element = ImageElement('example.jpg')
    image_element.on_created()
    print(image_element.render())


    container_element = ContainerElement('div')
    container_element.add_child(text_element)
    container_element.add_child(image_element)
    container_element.on_created()
    print(container_element.render())


    text_element.set_state(HiddenState())
    text_element.on_removed()
    print(text_element.get_state().handle())
