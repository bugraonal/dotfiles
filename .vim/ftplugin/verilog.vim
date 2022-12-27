set tabstop=4
set expandtab
set autoindent


let b:ale_linters = ['xvlog']

autocmd VimLeave * : execute '!rm ' . expand('%:p:h') . '/xvlog.log'
autocmd VimLeave * : execute '!rm ' . expand('%:p:h') . '/xvlog.pb'
autocmd VimLeave * : execute '!rm -rf ' . expand('%:p:h') . '/xsim.dir'
