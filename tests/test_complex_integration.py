from src.models import Apartment
from src.manager import Manager
from src.models import Parameters

def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key


def testy():
    parameters = Parameters()
    manager = Manager(parameters)

    assert manager.get_apartment_costs('A1', 2024, 3) == 450.0
    assert manager.get_apartment_costs('A1', 2024, 3) == 450.0
    assert manager.get_apartment_costs('A1', 2024, 3) == 450.0