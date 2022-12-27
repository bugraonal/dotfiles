# PATH
export PATH=$PATH:$HOME/.local/bin
export EDITOR=vim
export OPENRAM_HOME="$HOME/UCSC/tools/PrivateRAM/compiler"
export OPENRAM_TECH="$HOME/UCSC/tools/PrivateRAM/technology"
export PYTHONPATH="$PYTHONPATH:$OPENRAM_HOME"
export FREEPDK45="/software/PDKs/FreePDK45"
export PATH=$PATH:$HOME/.scripts
export PATH=$PATH:$HOME/UCSC/tools/Xilinx/Vivado/2019.1/bin
. "$HOME/.cargo/env"

# Java blank window fix
export _JAVA_AWT_WM_NONPARENTING=1

# Alias
alias pdf=zathura
alias open=mimeo
alias donut="ssh bonal@donut.soe.ucsc.edu"
