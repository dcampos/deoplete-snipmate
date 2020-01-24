from deoplete.base.source import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = "snipmate"
        self.mark = "[snip]"
        self.rank = 8
        self.is_volatile = True

    def gather_candidates(self, context):
        suggestions = []
        word = self.vim.eval('snipMate#WordBelowCursor()')
        snippets = self.vim.eval(
            "snipMate#GetSnippetsForWordBelowCursorForComplete('{}')".format(context['complete_str']))
        for snippet in snippets:
            suggestions.append(
                {
                    "word": snippet['word'],
                    "menu": self.mark + " " + snippet['menu'],
                    "dup": 1,
                    "kind": "snippet",
                }
            )
        return suggestions
