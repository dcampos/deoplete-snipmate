from deoplete.base.source import Base
from functools import lru_cache
import json
import re

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = "snipmate"
        self.mark = "[SM]"
        self.rank = 1000
        self.is_volatile = True

    def gather_candidates(self, context):
        suggestions = []
        word = context['complete_str']
        snippets = self.vim.eval(
            "snipMate#GetSnippetsForWordBelowCursor('{}', 0)".format(word))
        for [word, data] in snippets:
            for desc, [snip, version] in data.items():
                user_data = json.dumps({'snippet': snip, 'version': version})
                if version == 1:
                    ft = desc[:desc.find(' ')]
                    menu_preview = '[{}] {}'.format(ft, self._make_preview(snip))
                else:
                    menu_preview = desc
                suggestions.append(
                    {
                        "word": word,
                        "menu": self.mark + ' ' + menu_preview,
                        "dup": 1,
                        "kind": "snippet",
                        "user_data": user_data
                    }
                )
        return suggestions

    @lru_cache()
    def _make_preview(self, snippet):
        snippet = snippet.replace('"', '\\"')
        [tokens, _] = self.vim.eval('snipmate#parse#snippet("{}")'.format(snippet))
        preview_lines = []
        for line in tokens:
            preview_line = ''
            for item in line:
                if type(item) is list:
                    preview_line += '…'
                else:
                    preview_line += item
            preview_lines.append(preview_line)
        preview = str.join(' ', preview_lines)
        preview = re.sub(r'\s+', ' ', preview)
        return preview
