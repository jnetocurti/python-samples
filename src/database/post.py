class Post():

    def __init__(self, subject, content, id=None):
        self._id = id
        self._subject = subject
        self._content = content

    @property
    def id(self):
        return self._id

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        self._subject = subject

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content
