
call plug#begin()

Plug 'VundleVim/Vundle.vim'

"" Status bar at bottom
Plug 'vim-airline/vim-airline'

Plug 'edkolev/promptline.vim'

"" Cool color scheme
Plug 'croaker/mustang-vim'

"" File navigation tree
Plug 'preservim/nerdtree'

"" Auto complete using clang
"Plug 'xavierd/clang_complete'

"" Linter, fixer, auto-complete...
Plug 'dense-analysis/ale'

"" Python DocString
Plug 'heavenshell/vim-pydocstring'

"" Auto-complete framework
if has('nvim')
  Plug 'Shougo/deoplete.nvim', {'do': 'UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif

"Plug 'deoplete-plugins/deoplete-clang'
Plug 'tweekmonster/deoplete-clang2'
Plug 'Shougo/neoinclude.vim'

"" Tags viewer
Plug 'majutsushi/tagbar'

"" YouCompleteMe
Plug 'ycm-core/YouCompleteMe'

"" VimWiki
Plug 'vimwiki/vimwiki'

call plug#end()

set encoding=utf-8

" Deoplete
let g:deoplete#enable_at_startup = 0
"call deoplete#custom#option('sources', {
"\ '_': ['ale', 'buffer', 'tag'],
"\})
"call deoplete#custom#source('ale', 'rank', '999')

" Deoplete Clang
"let g:deoplete#sources#clang#libclang_path='/usr/lib/llvm-6.0/lib/libclang.so'
"let g:deoplete#sources#clang#clang_header='/usr/lib/llvm-6.0/lib/clang/6.0.0/include'



let g:airline_powerline_fonts = 1
let mapleader = ","

let g:clang_library_path='/usr/lib/llvm-6.0/lib/libclang.so.1'
let g:airline#extensions#ale#enabled = 1
let g:ale_java_eclipselsp_path='/home/bugra/sources/eclipse.jdt.ls'

let g:pydocstring_doq_path='/home/bugra/.local/bin/doq'
let g:pydocstring_fromatter='numpy'

" Clipboard functions
nnoremap <leader>y "*y
nnoremap <leader>Y "+y
nnoremap <leader>p "*p
nnoremap <leader>P "+p

" Background fix for xterm-kitty
set t_ut=

" Use to see speacial chars
set listchars=eol:¬,tab:>-,trail:~,extends:>,precedes:<,space:⌴

" Navigate tabs
nnoremap <C-Left> : tabp <CR>
nnoremap <C-Right> : tabn <CR>

set number relativenumber
syntax on
set backspace=indent,eol,start
highlight LineNR cterm=NONE ctermfg=DarkGrey ctermbg=NONE

command -nargs=1 CopyAboveAndPaste execute "normal! y<args>k<args>jp"
nnoremap <C-y> : CopyAboveAndPaste 

colo mustang

set hlsearch

" Load all plugins now.
" Plugins need to be added to runtimepath before helptags can be generated.
packloadall
" Load all of the helptags now, after plugins have been loaded.
" All messages and errors will be ignored.
silent! helptags ALL

function! ToggleGUICruft()
  if &guioptions=='i'
    exec('set guioptions=imTrL')
  else
    exec('set guioptions=i')
  endif
endfunction

map <c-F11> <Esc>:call ToggleGUICruft()<cr>

" by default, hide gui menus
set guioptions=i
set showcmd
set tabstop=4
set expandtab
set exrc
set secure
