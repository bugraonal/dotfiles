" ========= Plugins =========
call plug#begin()

"" Status bar at bottom
Plug 'vim-airline/vim-airline'

Plug 'edkolev/promptline.vim'

"" Cool color scheme
Plug 'croaker/mustang-vim'

"" Extend % operation
Plug 'adelarsq/vim-matchit'

"" File navigation tree
Plug 'preservim/nerdtree'
Plug 'PhilRunninger/nerdtree-visual-selection'
Plug 'PhilRunninger/nerdtree-buffer-ops'

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

"" Git plugin
Plug 'tpope/vim-fugitive'

"" VimWiki
Plug 'vimwiki/vimwiki'

"" fzf
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'

"" markdown perview
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}

"" latex syntax and preview
Plug 'lervag/vimtex'

"" Indent line
Plug 'Yggdroot/indentLine'

"" Repeat custom commands
Plug 'tpope/vim-repeat'

"" Surround utility
Plug 'tpope/vim-surround'

"" Comment utility
Plug 'tpope/vim-commentary'

call plug#end()

" ========= Plugin Options =========
"" ALE Options
let g:ale_completion_enabled = 1
let g:ale_completion_autoimport = 1
let g:airline#extensions#ale#enabled = 1
set omnifunc=ale#completion#OmniFunc
"" Disable inline errors
let g:ale_virtualtext_cursor = 0
"" Show ale hover info in bubble
let g:ale_floating_preview = 1

let g:airline_powerline_fonts = 1

"" PyDocString
let g:pydocstring_doq_path='/home/bugra/.local/bin/doq'
let g:pydocstring_fromatter='numpy'

"" Indent line customization
let g:indentLine_char = '│'

" Clipboard functions
let mapleader = ","
nnoremap <leader>y "*y
nnoremap <leader>Y "+y
nnoremap <leader>p "*p
nnoremap <leader>P "+p

" ========= Appearance Customizations =========
" Background fix for xterm-kitty
set t_ut=

" Use to see speacial chars
set listchars=eol:¬,tab:>-,trail:~,extends:>,precedes:<,space:⌴

highlight LineNR cterm=NONE ctermfg=DarkGrey ctermbg=NONE
highlight Pmenu ctermfg=DarkGrey ctermbg=Darkgrey
colo desert

" ========= Shortcuts =========
" Navigate tabs
nnoremap gh : tabp <CR>
nnoremap gl : tabn <CR>

" New line in normal mode
nnoremap <Enter> o<ESC>k
nnoremap <S-Enter> O<ESC>j

" Fuzzy
nnoremap ff : Files <CR>
nnoremap fb : Buffers <CR>

" Navigate buffers
nnoremap gn : bn <CR>
nnoremap gm : bp <CR>

" NERDTree shortcuts
nnoremap <C-S-N> : NERDTreeToggle <CR>

" ALE goto
nmap <silent> gk <Plug>(ale_previous_wrap)
nmap <silent> gj <Plug>(ale_next_wrap)
nmap <silent> gd <Plug>(ale_go_to_definition)

packloadall
silent! helptags ALL

" For gvim
function! ToggleGUICruft()
  if &guioptions=='i'
    exec('set guioptions=imTrL')
  else
    exec('set guioptions=i')
  endif
endfunction
map <c-F11> <Esc>:call ToggleGUICruft()<cr>

" ========= Options =========
" Return to last edit position when opening files (You want this!)
autocmd BufReadPost *
     \ if line("'\"") > 0 && line("'\"") <= line("$") |
     \   exe "normal! g`\"" |
     \ endif

set hlsearch
set number relativenumber
syntax on
set backspace=indent,eol,start
set encoding=utf-8
" by default, hide gui menus
set guioptions=i
set showcmd
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set exrc
set secure
set incsearch
set scrolloff=5
