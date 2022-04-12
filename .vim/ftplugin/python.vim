
let b:ale_linters = ['flake8']

let g:ale_python_flake8_options = '--ignore=E501,E127,E225,E261,E221,E408,E402,F405,E401' 

let b:ale_fixers = ['autopep8']

let g:pydocstring_formatter = 'numpy'
