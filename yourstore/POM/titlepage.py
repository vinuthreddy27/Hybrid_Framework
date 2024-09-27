from yourstore.library.library import Base

class Title(Base):
    title_locator=("xpath","//title[.='Your Store']")

    def title_verification(self):
        self.search_for_element(self.title_locator)
