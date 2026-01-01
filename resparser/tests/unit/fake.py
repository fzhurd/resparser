from resparser.com.parser.file_parser import FileParser


class FakeParser(FileParser):
    def parse(self, file_path: str) -> str:
        return """
        Jane Doe
        Email: jane.doe@gmail.com
        Python Machine Learning
        """
