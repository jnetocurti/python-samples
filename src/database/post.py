class Post():

    def __init__(self, **kwargs):
        self._id = kwargs.get('id')
        self._subject = kwargs.get('subject')
        self._content = kwargs.get('content')

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
