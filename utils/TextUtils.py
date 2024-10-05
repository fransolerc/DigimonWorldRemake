import re


class TextUtils:
    @staticmethod
    def extract_text(text):
        match = re.search(r'NSLOCTEXT\(\s*"[^"]*"\s*,\s*"[^"]*"\s*,\s*"([^"]*)"\s*\)', text)
        if match:
            extracted_text = match.group(1)
            extracted_text = extracted_text.replace("\\'", "'")
            return extracted_text
        return text
