import requests
import json
from pathlib import Path

FILE = Path(__file__).resolve().parent / "static" / "data.json"

CATEGORIES = ["drought","floods","landslides","wildfires","severeStorms"]
DATES = { 'start': '2021-01-01', 'end': '2025-12-31'}
BBOX = {
	'min_lon': -95,
	"min_lat": 5,
	"max_lon": -75,
	"max_lat": 25
}

def load_json():
	file = Path(__file__).resolve().parent / "static" / "data.json"

	url = (
		f"https://eonet.gsfc.nasa.gov/api/v3/events"
		f"?start={DATES['start']}&end={DATES['end']}"
		f"&category=" + ",".join(CATEGORIES)
		f"&bbox={",".join(BBOX.values())}"
	)

	res = requests.get(url)
	data = res.json()
        
	with open(file, "w", encoding="utf-8") as f:
		json.dump(data, f, indent=2)

def get_data():
	with open(FILE, 'r') as f:
		data = json.load(f)
	
	return data

load_json()