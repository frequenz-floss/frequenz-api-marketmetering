# License: MIT
# Copyright © 2025 Frequenz Energy-as-a-Service GmbH

"""Generate the code reference pages."""

import mkdocs_gen_files
from frequenz.repo.config.mkdocs import api_pages

api_pages.generate_python_api_pages("py", "python-reference")

# We need to remove the generated gRPC files from the documentation because they
# cause issues with mkdocstrings/griffe (warnings about missing type hints).
# We can't easily exclude them in generate_python_api_pages, so we overwrite
# the generated markdown files with a placeholder.
try:
    with mkdocs_gen_files.open(
        "python-reference/frequenz/api/marketmetering/v1alpha1/marketmetering_pb2_grpc.md",
        "w",
    ) as f:
        print("<!-- This file is excluded from documentation generation -->", file=f)
except FileNotFoundError:
    pass

api_pages.generate_protobuf_api_pages()
