
let b:ale_linters = ['pylsp']
let b:ale_fixers = ['trim_whitespace', 'remove_trailing_lines', 'autopep8']

let g:ale_python_pylsp_config = 
                        \{
                        \   'pylsp': {
                        \       'plugins': {
                        \           'pycodestyle': {'enabled': v:false},
                        \           'pyflakes': {'enabled': v:false},
                        \           'flake8': {'enabled': v:true,
                        \               'ignore': ['E501', 'E127', 'E225', 'E261', 'E221', 'E408', 'E402', 'F405', 'F403', 'E401', 'W503']}
                        \       }
                        \   }
                        \}


let g:pydocstring_formatter = 'numpy'
