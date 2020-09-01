import covidcast
from datetime import date
from matplotlib import pyplot as plt
data = covidcast.signal("fb-survey", "smoothed_cli", start_day = date(2020,8,3), end_day = date(2020,8,4), geo_type = "state")
covidcast.plot_choropleth(data)
plt.show()