# INDEX
def test_index_no_params(test_client):
    response = test_client.get("/index")
    assert response.status_code == 200
    assert response.json() == {"index": 135.61}  # September 2021


def test_index_1996(test_client):
    response = test_client.get("/index?year=1996")
    assert response.status_code == 200
    assert response.json() == {"index": 154.29}  # September 2021


def test_index_2013(test_client):
    response = test_client.get("/index?year=2013")
    assert response.status_code == 200
    assert response.json() == {"index": 112.29}  # September 2021


def test_index_2020(test_client):
    response = test_client.get("/index?year=2020")
    assert response.status_code == 400
    assert response.json() == {"detail": "WRONG_YEAR"}


# ZIPCODE
def test_zipcode(test_client):
    response = test_client.get("/zipcodes/9000")
    assert response.status_code == 200
    assert response.json() == {"risk_factor": "B"}


def test_zipcode_too_high(test_client):
    response = test_client.get("/zipcodes/10000")
    assert response.status_code == 400
    assert response.json() == {"detail": "ZIPCODE_NOT_VALID"}


def test_zipcode_too_low(test_client):
    response = test_client.get("/zipcodes/999")
    assert response.status_code == 400
    assert response.json() == {"detail": "ZIPCODE_NOT_VALID"}


def test_zipcode_low_bound(test_client):
    response = test_client.get("/zipcodes/9170")
    assert response.status_code == 200
    assert response.json() == {"risk_factor": "A"}


def test_zipcode_high_bound(test_client):
    response = test_client.get("/zipcodes/9240")
    assert response.status_code == 200
    assert response.json() == {"risk_factor": "A"}


def test_zipcode_middle(test_client):
    response = test_client.get("/zipcodes/9200")
    assert response.status_code == 200
    assert response.json() == {"risk_factor": "A"}
