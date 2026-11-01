# Python
python -m venv .venv
source .venv/bin/activate
pip install rustimport juliacall numba


# Ocaml
opam switch create . 4.14.2
eval $(opam env)
opam install -y ocaml-in-python

#
pip install ./_opam/lib/ocaml-in-python
# why ?
cp _opam/lib/ocaml-in-python/ocaml/ocaml_in_python.so .venv/lib/python3.10/site-packages/ocaml/
