# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent


def load_csv(filename):
    path = DATA_DIR / filename
    if not path.is_file():
        raise FileNotFoundError(
            f"Missing data file: {path}\n"
            f"Place {filename} in the same folder as this Python script."
        )
    return np.genfromtxt(
        path,
        delimiter=',',
        skip_header=1,
        dtype=str
    )


def load_streamflow(filename):
    """Load streamflow dates and gauge readings from a CSV file."""
    data = load_csv(filename)
    dates = pd.to_datetime(data[:, 0])
    flows = data[:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot streamflow values at each gauge."""
    colors = ['purple', 'teal', 'green', 'orange', 'orangered']

    plt.figure(figsize=(10, 6))
    for i, site in enumerate(sites):
        plt.plot(dates, flows[:, i], label=site,
                 color=colors[i % len(colors)])

    plt.title('Provo River Streamflow Data (2021)', fontsize=18)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Flowrate (cfs)', fontsize=12)
    plt.legend(title='Site Numbers')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



L = 6      # ft
RA = 170   # lb
RB = 410   # lb
P1 = 100   # lb
q1 = 120   # lb/ft
q2 = 120   # lb/ft

x = np.linspace(0, L, 500)

V = np.zeros_like(x)

for i in range(len(x)):
    if x[i] < 2:
        V[i] = RA - q1 * x[i]

    elif x[i] < 4:
        V[i] = RA - (q1 * 2) - P1

    else:
        V[i] = RA - (q1 * 2) - P1 + RB - q2 * (x[i] - 4)

plt.figure(figsize=(10,6))
plt.plot(x, V, linewidth=2)

plt.fill_between(x, V, 0, alpha=0.3)

plt.axhline(0, color='black')

plt.title('Shear Diagram')
plt.xlabel('x (ft)')
plt.ylabel('V (lb)')
plt.grid(True)

plt.show()


L = 6      # ft
RA = 170   # lb
RB = 410   # lb
P1 = 100   # lb
q1 = 120   # lb/ft
q2 = 120   # lb/ft

x = np.linspace(0, L, 500)

M = np.zeros_like(x)

for i in range(len(x)):
    if x[i] < 2:
        M[i] = (RA * x[i]) - (q1 * x[i]**2 / 2)

    elif x[i] < 4:
        M[i] = (RA * x[i]) \
               - (q1 * 2 * (x[i] - 1)) \
               - (P1 * (x[i] - 2))

    else:
        M[i] = (RA * x[i]) \
               - (q1 * 2 * (x[i] - 1)) \
               - (P1 * (x[i] - 2)) \
               + (RB * (x[i] - 4)) \
               - (q2 * (x[i] - 4) * ((x[i] - 4) / 2))

plt.figure(figsize=(10,6))
plt.plot(x, M, linewidth=2, color='red')

plt.fill_between(x, M, 0, color='red', alpha=0.3)

plt.axhline(0, color='black')

plt.title('Moment Diagram')
plt.xlabel('x (ft)')
plt.ylabel('M (lb-ft)')
plt.grid(True)

plt.show()


data = load_csv('2013-2014-Pasadena-Temperature-Data.csv')

import pandas as pd

x = pd.to_datetime(data[:,0])
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)


plt.figure(figsize=(10, 6))

plt.plot(x, y_1, label='High Temperature',
         color='orangered', linewidth=2)

plt.plot(x, y_2, label='Low Temperature',
         color='teal', linewidth=2)
plt.title('Pasadena Temperature Data 2013-2014', fontsize=18)
plt.xlabel('Date')
plt.ylabel('Degrees (Fahrenheit)')

plt.legend()
plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



data = load_csv('Fremont-Bridge-Bicycle-Count.csv')

import pandas as pd

x = pd.to_datetime(data[:,0])

y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)


plt.figure(figsize=(10, 6))

plt.plot(x, y_1, label='Fremont Bridge Total',
         color='cadetblue', linewidth=2)

plt.plot(x, y_3, label='Fremont Bridge West Sidewalk',
         color='darkred', linewidth=2)

plt.plot(x, y_2, label='Fremont Bridge East Sidewalk',
         color='darkorange', linewidth=2)

plt.title('Fremont Bridge Bicycle Count')
plt.xlabel('Date')
plt.ylabel('Number of Bicycles')

plt.legend()
plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Bicycle counts appear lower in the later years because travel patterns
# changed significantly around 2020. More people worked from home and
# traveled less frequently, reducing the number of bicycle trips recorded
# at the bridge. Seasonal and data collection differences may also affect
# the counts.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = load_csv('2012-US-Birth-Rates.csv')

x = pd.to_datetime(data[:, 0])
y_1 = data[:, 1].astype(float)


plt.figure(figsize=(12, 4))

plt.plot(x, y_1, color='turquoise', linewidth=1.5)

plt.title('Average U.S. Daily Birth Data')
plt.xlabel('Date')
plt.ylabel('Births')

plt.grid(True)

plt.annotate(
    "New Year's Day",
    xy=(pd.Timestamp('2012-01-01'), 4000),
    xytext=(pd.Timestamp('2012-01-15'), 3900),
    arrowprops=dict(arrowstyle='->',
                    connectionstyle='arc3,rad=-0.3',
                    lw=2)
)

plt.annotate(
    '4th of July',
    xy=(pd.Timestamp('2012-07-04'), 4300),
    xytext=(pd.Timestamp('2012-08-05'), 4200),
    arrowprops=dict(arrowstyle='->',
                    connectionstyle='arc3,rad=-0.4',
                    lw=2)
)

plt.annotate(
    'Halloween',
    xy=(pd.Timestamp('2012-10-31'), 4680),
    xytext=(pd.Timestamp('2012-09-15'), 4600),
    arrowprops=dict(arrowstyle='->',
                    connectionstyle='arc3,rad=-0.4',
                    lw=2)
)

plt.annotate(
    'Thanksgiving',
    xy=(pd.Timestamp('2012-11-22'), 4475),
    xytext=(pd.Timestamp('2012-10-12'), 4280),
    arrowprops=dict(arrowstyle='->',
                    connectionstyle='arc3,rad=0.4',
                    lw=2)
)

plt.annotate(
    'Christmas',
    xy=(pd.Timestamp('2012-12-25'), 3850),
    xytext=(pd.Timestamp('2012-10-22'), 3900),
    arrowprops=dict(arrowstyle='->',
                    connectionstyle='arc3,rad=0.5',
                    lw=2)
)

plt.tight_layout()
plt.show()

# Birth rates may drop on major holidays because fewer scheduled
# births and medical procedures are performed on those days.
# Hospitals often postpone elective inductions and C-sections until
# after the holiday, reducing the number of births recorded.


if __name__ == '__main__':
    sites = ['10163000', '10155200', '10155500', '10154200', '10155000']
    dates, flows = load_streamflow(
        'June-2021-Provo-River-Streamflow-Rates.csv'
    )
    plot_streamflow(dates, flows, sites)