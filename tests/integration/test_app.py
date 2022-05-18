# INDEX
def test_index_no_params(test_client):
    response = test_client.get("/index")
    assert response.status_code == 200
    assert response.json() == {"base_year": 2004, "index": 144.43}  # April 2022


def test_index_1996(test_client):
    response = test_client.get("/index?year=1996")
    assert response.status_code == 200
    assert response.json() == {"base_year": 1996, "index": 164.32}  # April 2022


def test_index_2013(test_client):
    response = test_client.get("/index?year=2013")
    assert response.status_code == 200
    assert response.json() == {"base_year": 2013, "index": 119.59}  # April 2022


def test_index_2020(test_client):
    response = test_client.get("/index?year=2020")
    assert response.status_code == 404
    assert response.json() == {"detail": "Year 2020 is not valid"}


# ZIPCODE
def test_zipcode(test_client):
    response = test_client.get("/zipcodes/9000")
    assert response.status_code == 200
    assert response.json() == {"zipcode": 9000, "risk_factor": "B", "exists": True}  # nopep8


def test_zipcode_too_high(test_client):
    response = test_client.get("/zipcodes/10000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Zipcode 10000 is not valid"}


def test_zipcode_too_low(test_client):
    response = test_client.get("/zipcodes/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Zipcode 999 is not valid"}


def test_zipcode_low_bound(test_client):
    response = test_client.get("/zipcodes/9170")
    assert response.status_code == 200
    assert response.json() == {"zipcode": 9170, "risk_factor": "A", "exists": True}  # nopep8


def test_zipcode_high_bound(test_client):
    response = test_client.get("/zipcodes/9240")
    assert response.status_code == 200
    assert response.json() == {"zipcode": 9240, "risk_factor": "A", "exists": True}  # nopep8


def test_zipcode_middle(test_client):
    response = test_client.get("/zipcodes/9200")
    assert response.status_code == 200
    assert response.json() == {"zipcode": 9200, "risk_factor": "A", "exists": True}  # nopep8
