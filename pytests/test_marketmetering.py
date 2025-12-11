# License: MIT
# Copyright © 2025 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.marketmetering package."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api import marketmetering

    assert marketmetering is not None


def test_module_import_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.marketmetering.v1alpha1 import marketmetering_pb2

    assert marketmetering_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.marketmetering.v1alpha1 import marketmetering_pb2_grpc

    assert marketmetering_pb2_grpc is not None
