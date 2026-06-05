# Python
python -m venv .venv
source .venv/bin/activate
pip install llvmlite 


# Ocaml
opam switch create . 4.14.2
eval $(opam env)
opam install -y ocaml-in-python llvm

#
pip install ./_opam/lib/ocaml-in-python
