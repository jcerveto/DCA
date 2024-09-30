class KeywordException(Exception):
    def __init__(self, keyword: str):
        super().__init__(f'Keyword "{keyword}" was pressed. ')
        self.keyword = keyword
