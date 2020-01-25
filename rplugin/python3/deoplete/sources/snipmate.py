from deoplete.base.source import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = "snipmate"
        self.mark = "[SM]"
        self.rank = 8
        self.is_volatile = True

    def gather_candidates(self, context):
        suggestions = []
        self.vim.out_write('complete_str: ' + context['complete_str'] + "\n")
        word = context['complete_str']
        snippets = self.vim.eval(
            "snipMate#GetSnippetsForWordBelowCursor('{}', 0)".format(word))
        for snippet in snippets:
            for desc, value in snippet[1].items():
                suggestions.append(
                    {
                        "word": snippet[0],
                        "menu": self.mark + ' ' + desc,
                        "dup": 1,
                        "kind": "snippet",
                        "user_data": value[0]
                    }
                )
        return suggestions
