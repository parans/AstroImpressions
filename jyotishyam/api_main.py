from fastapi import FastAPI
from fastapi import Response

import chart_calc.mod_lagna as mod_lagna
import drawCharts.mod_drawChart as dc
import mod_astrocharts as mdata
import mod_json as js
import json
import log_utils

app = FastAPI()
logger = log_utils.getLogger(__name__)  

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/birthChart/details")
async def chart_details(bday: mdata.BirthDetails):
    logger.info("Birth details")
    charts = mdata.VedicCharts()
    mod_lagna.compute_lagna_Chart(bday, charts)
    res = json.dumps(charts.to_dict(), indent=4)
    return Response(content=res, media_type="application/json")

@app.post("/birthChart/svg")
async def chart(bday: mdata.BirthDetails):
    charts = mdata.VedicCharts()
    mod_lagna.compute_lagna_Chart(bday, charts)
    js.load_drawChartConfig()
    res = dc.gen_SVG(charts.D1)
    return Response(content=res, media_type="image/svg+xml")  