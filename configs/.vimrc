set nocompatible
set hidden

set smartcase

let mapleader=","
set history=1000
set undolevels=500

runtime macros/matchit.vim

set wildmenu
set wildmode=list:longest
set visualbell

set title

set ruler
nmap <silent> <leader>n :set number!<CR>

syntax on

set hlsearch
set incsearch

nmap <silent> <leader>s :set nolist!<CR>

set pastetoggle=<F2>
set showmode

set autochdir

nnoremap <leader>q :q<CR>
nnoremap <leader>w :w<CR>
