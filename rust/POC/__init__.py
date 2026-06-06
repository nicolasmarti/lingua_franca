import rustimport
rustimport.settings.compile_on_import = True
rustimport.settings.compile_release_binaries = True
import rustimport.import_hook
from .rustfib import fibonacci
