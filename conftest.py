def pytest_addoption(parser):
    parser.addoption("--index", action="store", type=int, help="El índice del elemento a seleccionar")