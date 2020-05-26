# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

PATH="/tools/Xilinx/Vivado/2018.3/bin:$PATH"

PATH="/tools/Xilinx/SDK/2018.3/bin:$PATH"

PATH="$HOME/tools/eclipse:$PATH"

PATH="$HOME/tools/Qt/Tools/QtCreator/bin:$PATH"
PATH="$HOME/scripts:$PATH"

PATH="$HOME/tools/Xilinx/14.7/ISE_DS/ISE/bin/lin64:$PATH"


export QSYS_ROOTDIR="/home/bugra/tools/intelFPGA/17.1/quartus/sopc_builder/bin"

export TERMCMD="terminator"

export QCUSTOMPLOT_PATH="$HOME/tools/qcustomplot"

export RANGER_LOAD_DEFAULT_RC="FALSE"

export TERM="xterm-kitty"

PATH="$PATH:/home/bugra/thesis/Compiler/ClangAction/scripts/build/bin"
