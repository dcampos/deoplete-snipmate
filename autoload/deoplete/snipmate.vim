" File: autoload/deoplete/snipmate.vim
" Description: Useful functions.


func! deoplete#snipmate#get_completion_item(user_data) abort
    if has_key(a:user_data, 'lspitem')
        " vim-lsp
        return a:user_data.lspitem
    elseif has_key(a:user_data, 'nvim')
        " nvim-lsp
        try
            return a:user_data.nvim.lsp.completion_item
        catch /^Vim\%((\a\+)\)\=:E716/
        endtry
    endif
    return {}
endfunc

func! deoplete#snipmate#try_expand() abort
    let s:snippet_data = {}
    let l:user_data = get(v:completed_item, 'user_data', {})
    let l:snippet = ''
    let l:version = 1
    if !empty(user_data)
        if type(user_data) != v:t_dict
            silent! let user_data = json_decode(user_data)
        endif

        if type(user_data) != v:t_dict
            return
        endif

        if has_key(user_data, 'snippet')
            let snippet = user_data.snippet
            let l:version = user_data.version
        else
            let lspitem = deoplete#snipmate#get_completion_item(user_data)
            if has_key(lspitem, 'textEdit') && type(lspitem.textEdit) == v:t_dict
                let snippet = lspitem.textEdit.newText
            elseif get(lspitem, 'insertTextFormat', -1) == 2
                let snippet = get(lspitem, 'insertText', '')
            endif
        endif

        if snippet ==# ''
            return
        endif

        let l:word = v:completed_item['word']
        let s:snippet_data = {'version': l:version, 'snippet': l:snippet, 'word': l:word}

        silent call feedkeys("\<c-r>=deoplete#snipmate#_expand()\<cr>", 'n')
    endif
endfunc

func! deoplete#snipmate#_expand() abort
    echo ''
    let &undolevels = &undolevels
    let word = s:snippet_data.word
    let col = col('.') - len(word)
    silent exe 's/\V' . escape(word, '/\.') . '\%#//'
    return snipMate#expandSnip(s:snippet_data.snippet, s:snippet_data.version, col)
endfunc
