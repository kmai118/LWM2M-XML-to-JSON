import xmltodict
import json
# Read the XML file
with open('imput.xml') as xml_file:
    xml_data = xml_file.read()
# Convert XML to Python dict
data_dict = xmltodict.parse(xml_data)
# Convert dict to JSON string
json_data = json.dumps(data_dict, indent=4)
# Save to a JSON file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)
print("Conversion complete! Saved as output.json")

