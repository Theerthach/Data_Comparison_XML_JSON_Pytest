import pytest
import json
from xml.etree import ElementTree as ET
from xml_aws import read_xml_from_s3  # Import function to read XML from S3
from json_api import read_json_from_local  # Import function to read JSON from local

# Define test parameters
S3_BUCKET = "testlocxml"
XML_FILE_KEY = "order1.xml"
LOCAL_JSON_FILE_PATH = "scr/order1.json"

@pytest.fixture
def load_files():
    """Fixture to load XML from S3 and JSON from local system"""
    xml_root = read_xml_from_s3(S3_BUCKET, XML_FILE_KEY)  # Already an XML Element
    json_content = read_json_from_local(LOCAL_JSON_FILE_PATH)  # Read JSON from local

    return xml_root, json_content
   

def test_order_id(load_files):
    """Test if order IDs match in XML and JSON"""
    xml_root, json_data = load_files

    xml_order_id = xml_root.find(".//Order").attrib["id"]
    json_order_id = json_data["Orders"]["Order"]["id"]

    assert xml_order_id == str(json_order_id), f"Order ID mismatch: XML({xml_order_id}) != JSON({json_order_id})"

def test_customer_info(load_files):
    """Test if customer details match"""
    xml_root, json_data = load_files

    xml_customer = xml_root.find(".//Customer")
    json_customer = json_data["Orders"]["Order"]["Customer"]

    assert xml_customer.find("CustomerID").text == str(json_customer["CustomerID"])
    assert xml_customer.find("Name").text == json_customer["Name"]
    assert xml_customer.find("Email").text == json_customer["Email"]
    assert xml_customer.find("Phone").text == json_customer["Phone"]

def test_order_details(load_files):
    """Test if order details (date & total amount) match"""
    xml_root, json_data = load_files

    xml_order_date = xml_root.find(".//OrderDate").text
    json_order_date = json_data["Orders"]["Order"]["OrderDetails"]["OrderDate"]

    xml_total_amount = xml_root.find(".//TotalAmount").text
    json_total_amount = json_data["Orders"]["Order"]["OrderDetails"]["TotalAmount"]["value"]

    assert xml_order_date == json_order_date
    assert float(xml_total_amount) == float(json_total_amount)

def test_shipping_details(load_files):
    """Test if shipping details match"""
    xml_root, json_data = load_files

    xml_shipping = xml_root.find(".//Shipping")
    json_shipping = json_data["Orders"]["Order"]["Shipping"]

    assert xml_shipping.find("Method").text == json_shipping["Method"]
    assert xml_shipping.find("TrackingNumber").text == json_shipping["TrackingNumber"]

    xml_address = xml_shipping.find("Address")
    json_address = json_shipping["Address"]

    assert xml_address.find("Street").text == json_address["Street"]
    assert xml_address.find("City").text == json_address["City"]
    assert xml_address.find("State").text == json_address["State"]
    assert xml_address.find("Zip").text == str(json_address["Zip"])
    assert xml_address.find("Country").text == json_address["Country"]

def test_order_lines(load_files):
    """Test if order line details match"""
    xml_root, json_data = load_files

    xml_order_lines = xml_root.findall(".//OrderLine")
    json_order_lines = json_data["Orders"]["Order"]["OrderLines"]["OrderLine"]

    assert len(xml_order_lines) == len(json_order_lines), "Mismatch in order line count"

    for xml_line, json_line in zip(xml_order_lines, json_order_lines):
        assert xml_line.attrib["lineNumber"] == str(json_line["lineNumber"])
        assert xml_line.find(".//Product/ProductID").text == str(json_line["Product"]["ProductID"])
        assert xml_line.find(".//Product/Name").text == json_line["Product"]["Name"]
        assert xml_line.find(".//Product/Category").text == json_line["Product"]["Category"]
        assert int(xml_line.find("Quantity").text) == int(json_line["Quantity"])
        assert float(xml_line.find("UnitPrice").text) == float(json_line["UnitPrice"]["value"])
        assert float(xml_line.find("Discount").text) == float(json_line["Discount"]["value"])
