# Natural Hazard Monitoring Dashboard
42 Django pool to learn Django framework

Map + charts showing natural events over time.

Map features:

markers for events

popup with event details

filter by event type

Example popup:
'''
Wildfire
Location: California
Date: 2025-08-12
Source: NASA EONET
'''
---------------------------------

Source: https://eonet.gsfc.nasa.gov/

API call : eonet.gsfc.nasa.gov/api/v3/events?start=2021-01-01&end=2025-12-31&category=drought,floods,landslides,wildfires,severeStorms&bbox=92,-12,141,23

=> dates from 01-01-2020 to 31-12-2025
=> Natural weather events: drought, floods, landslides, severeStorms, wildfires
=> South east Asia bounding box : SW 92, -12 | NE 141, 23 (center: 120, -7)


central america : eonet.gsfc.nasa.gov/api/v3/events?start=2021-01-01&end=2025-12-31&category=drought,floods,landslides,wildfires,severeStorms&bbox=-127,0,-55,35

-----------------------------------

mall Feature That Would Impress Interviewers ⭐

Add time filtering.

Example:

Show events from:
[ Last 7 days ]
[ Last 30 days ]
[ Last year ]

This shows real monitoring capability, which is exactly what these platforms do.

Simple Tech Stack

Backend:

Django

Python requests

GeoJSON endpoint

Frontend:

Leaflet

Plotly or Chart.js

One Thing That Makes This Project Much Better

Instead of only showing raw events, add aggregation logic in Django.

Example:

/api/events
/api/events-by-type
/api/events-by-month

This shows data processing ability, not just visualization.

✅ If you'd like, I can also show you:

a very clean project idea that combines NASA events + development monitoring (this would look extremely relevant for this company)

a 3-day build plan for this exact project

the exact Leaflet + Plotly dashboard layout that would look impressive in an interview demo.