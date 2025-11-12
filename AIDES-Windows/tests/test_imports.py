def test_import_package():
    import aides
    assert hasattr(aides, "__version__")
