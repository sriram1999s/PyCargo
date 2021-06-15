def remove_prefix(text, prefix): # removes a prefix from text if exists
    if text.startswith(prefix):
        return text[len(prefix):]
    return text
