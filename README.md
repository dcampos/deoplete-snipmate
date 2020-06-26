# deoplete-snipmate

A deoplete source for snipmate snippets.

# Overview

A [Deoplete][] source for [SnipMate][].

It also supports expanding snippets present in completion items provided by
some LSP servers. For this to work, a compatible client should be used, like
Neovim's built-in client or [vim-lsp][]. See also [deoplete-vim-lsp][] and
[deoplete-lsp][], but you can even use this feature without using deoplete.

[Deoplete]: https://github.com/Shougo/deoplete.nvim/
[Snipmate]: https://github.com/garbas/vim-snipmate
[vim-lsp]: https://github.com/prabirshrestha/vim-lsp
[deoplete-lsp]: https://github.com/Shougo/deoplete-lsp
[deoplete-vim-lsp]: https://github.com/lighttiger2505/deoplete-vim-lsp

## Installation

Use your favorite plugin manager.

To install it with vim-plug, first install Deoplete, then add this to your vimrc:

```vim
Plug 'dcampos/deoplete-snipmate'
```

## Usage

To have snippets expanded after completion without the need to press `Tab` or
whichever key you use to expand snippets normally, you may set up an `autocmd` for
expanding it automatically:

```vim
augroup vimrc
    autocmd!
    autocmd vimrc CompleteDone * call deoplete#snipmate#try_expand()
augroup END
```
