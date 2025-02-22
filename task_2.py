from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        for word in strings:
            self.put(word)
        current = self.root
        longest_prefix = ""
        while current and len(current.children) == 1 and current.value is None:
            char = next(iter(current.children))
            longest_prefix += char
            current = current.children[char]
        return longest_prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
